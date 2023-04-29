from django.shortcuts import redirect

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