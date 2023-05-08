from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

from posts.models import (Post,)

class RedirectHomeIfLogInMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)


class RedirectHomeIfNotAdminMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return redirect('home:home')
        if not self.request.user.is_admin:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

class RedirectHomeIfNotUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return redirect('home:home')
        if not self.request.user.is_user:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)


class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def handle_no_permission(self):
        # raise PermissionDenied
        return redirect('home:home')