from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from .forms import (UserForm, RegisterMemberUserForm, RegisterSectionForm)
from .models import (OrganizationUnit, OrganizationMember)
from .permissions import (RedirectHomeIfLogInMixin, RedirectHomeIfNotAdminMixin)

# Create your views here.
class Register(RedirectHomeIfLogInMixin, FormView):
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


class RegisterMember(LoginRequiredMixin, RedirectHomeIfNotAdminMixin, FormView):
    template_name = "accounts/register_member.html"
    form_class = RegisterMemberUserForm
    success_url = reverse_lazy('accounts:register_member') #change this later

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_section_form'] = RegisterSectionForm(user=self.request.user)
        return context

    def form_valid(self, form):
        register_section_form = RegisterSectionForm(self.request.POST, self.request.FILES)
        if all([form.is_valid(), register_section_form.is_valid()]):
        # if register_section_form.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            organization_member = register_section_form.save(commit=False, user=self.request.user)
            organization_member.member = user
            organization_member.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'register_section_form': RegisterSectionForm(self.request.POST, self.request.FILES)})


class Login(RedirectHomeIfLogInMixin, LoginView):
    template_name = "accounts/login.html"


class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home:index')