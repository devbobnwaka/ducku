import uuid
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

from accounts.models import (Section,)

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, max_length=200)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    cover_img = models.ImageField(upload_to="cover_img", blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    visibility = models.ManyToManyField(Section)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post-detail', args=[str(self.slug)])

    def get_absolute_edit_url(self):
        return reverse('post:post-update', args=[str(self.slug)])

    def get_absolute_delete_url(self):
        return reverse('post:post-delete', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)
            qs = Post.objects.filter(slug=self.slug).exclude(id=self.id)
            if qs.exists():
                self.slug = f"{self.slug}-{uuid.uuid4()}"
        super(Post, self).save(*args, **kwargs)
        if self.slug == '':
            self.slug = uuid.uuid4()
            qs = Post.objects.filter(slug=self.slug).exclude(id=self.id)
            if qs.exists():
                self.slug = f"{self.slug}-{uuid.uuid4()}"
            self.save()