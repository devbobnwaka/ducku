from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import (User, OrganizationUnit, Section, OrganizationMember)


class UserForm(UserCreationForm):
    organization_name = forms.CharField(max_length=50)
    password1  = forms.CharField(widget=forms.PasswordInput())
    password2  = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'organization_name', 'password1', 'password2')


    def save_profile(self, commit=True):
        organization_unit = OrganizationUnit()
        organization_unit.name = self.cleaned_data.get('organization_name')
        if commit:
            organization_unit.save()
        return organization_unit


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        data = self.cleaned_data.get('name')
         # Check if the value already exists in the database
        if Section.objects.filter(name__iexact=data.lower(), organization=self.user.organizationunit).exists():
            raise ValidationError(f"{data} already exist")
        # If the value passes validation, return it
        return data


class RegisterMemberUserForm(UserCreationForm):
    password1  = forms.CharField(widget=forms.PasswordInput())
    password2  = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class RegisterSectionForm(forms.Form):
    section = forms.ModelChoiceField(queryset=Section.objects.all())



#     def save_profile(self, commit=True):
#         organization_unit = OrganizationUnit()
#         organization_unit.name = self.cleaned_data.get('organization_name')
#         if commit:
#             organization_unit.save()
#         return organization_unit

