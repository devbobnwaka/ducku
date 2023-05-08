from django import forms
from .models import Post
from accounts.models import (Section,)

class Visibility(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "sub_title", "cover_img", "body", "visibility"]
        widgets = {
            'visibility': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['visibility'].queryset = Section.objects.filter(organization=self.user.member.organization)
            # self.fields['section'].empty_label = 'Select user section'