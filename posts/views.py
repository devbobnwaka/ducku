from django.shortcuts import render
from accounts.models import (Section,)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


from .models import Post
from .forms import (Visibility,)
from accounts.permissions import (RedirectHomeIfNotUserMixin, UserIsOwnerMixin)


# Create your views here.
class PostCreateView(LoginRequiredMixin, RedirectHomeIfNotUserMixin, CreateView):
    model = Post
    form_class = Visibility
    # success_url = reverse_lazy('post:post-detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_header'] = "Create Post"
        return context

    def get_success_url(self):
        return reverse_lazy('post:post-detail', kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    def form_valid(self, form):
        form.instance.user = self.request.user
        if 'draft' in self.request.POST:
            return self.draft(form)
        elif 'publish' in self.request.POST:
            return self.publish(form)

    def draft(self, form):
        post = form.save(commit=False)
        post.is_published = False
        post.save()
        return super().form_valid(form)

    def publish(self, form):
        post = form.save(commit=False)
        post.is_published = True
        post.save()
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, RedirectHomeIfNotUserMixin, UserIsOwnerMixin, UpdateView):
    model = Post
    form_class = Visibility
    
    def get_success_url(self):
        return reverse_lazy('post:post-detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_header'] = "Update Post"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        if 'draft' in self.request.POST:
            return self.draft(form)
        elif 'publish' in self.request.POST:
            return self.publish(form)

    def draft(self, form):
        post = form.save(commit=False)
        post.is_published = False
        post.save()
        return super().form_valid(form)

    def publish(self, form):
        post = form.save(commit=False)
        post.is_published = True
        post.save()
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, RedirectHomeIfNotUserMixin, DetailView):
    model = Post
    context_object_name = 'post'



class PostListView(LoginRequiredMixin, RedirectHomeIfNotUserMixin, ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        # visibility = Section.objects.filter(organization=user.member.organization)
        return qs.filter(visibility=user.member.section, is_published=True)

class UserPostListView(LoginRequiredMixin, RedirectHomeIfNotUserMixin, ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user=user)


class PostDeleteView(UserIsOwnerMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home:home')


