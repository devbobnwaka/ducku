import uuid
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    #required fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email


class OrganizationUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.UUIDField(unique=True, editable=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        if self.unique_id is None:
            self.unique_id = uuid.uuid4()
            qs = OrganizationUnit.objects.filter(unique_id=self.unique_id).exclude(id=self.id)
            if qs.exists():
                self.unique_id = uuid.uuid4()
        super().save(*args, **kwargs)
        if self.unique_id is None:
            self.unique_id = uuid.uuid4()
            qs = OrganizationUnit.objects.filter(unique_id=self.unique_id).exclude(id=self.id)
            if qs.exists():
                self.unique_id = uuid.uuid4()
            self.save()


class Section(models.Model):
    organization = models.ForeignKey(OrganizationUnit, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class OrganizationMember(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    organization = models.ForeignKey(OrganizationUnit, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pic")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.member.username

    def get_organization_unit(self):
        return self.organization




