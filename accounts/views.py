from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from .forms import (UserForm, )
from .models import (OrganizationUnit,)

# Create your views here.
class Register(FormView):
    template_name = "accounts/register.html"
    form_class = UserForm
    success_url = reverse_lazy('accounts:login') #change this later

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            organization = OrganizationUnit(user=user, name=form.cleaned_data.get('organization_name'))
            organization.save()
        return super().form_valid(form)


class RegisterMember(FormView):
    template_name = "accounts/register_member.html"
    form_class = UserForm
    success_url = reverse_lazy('accounts:login') #change this later

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            organization = OrganizationUnit(user=user, name=form.cleaned_data.get('organization_name'))
            organization.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = "accounts/login.html"


class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home:index')