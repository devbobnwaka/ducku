from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView

from accounts.forms import SectionForm

# Create your views here.


class Section(LoginRequiredMixin, CreateView):
    template_name = "apps/add_section.html"
    form_class = SectionForm
    success_url = reverse_lazy('home:home') #change this later

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            section = form.save(commit=False)
            section.organization = self.request.user.organizationunit
            section.save()
            print('Section created!!!') 
            # try:
            #     section = form.save(commit=False)
            #     section.organization = self.request.user.organizationunit
        #         section.save()
        #         print('Section created!!!') 
        #     except IntegrityError as e:
        #         # Catch the IntegrityError exception and handle it appropriately
        #         if 'unique constraint' in str(e).lower():
        #             print("Error: Duplicate values violates unique constraint!")
        #             return super().form_valid(form)

        #         else:
        #             print("Error: " + str(e))
        #     except Exception as e:
        #         # Catch any other exceptions that may occur
        #         print("Error: " + str(e))
            # print(self.request.user.organizationunit)
            # print(dir(self.request.user))
        return super().form_valid(form)