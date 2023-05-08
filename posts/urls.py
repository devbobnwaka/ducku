from django.urls import path
from .views import (PostCreateView, PostDetailView, 
                    PostListView, PostUpdateView, 
                    UserPostListView, PostDeleteView)

app_name = 'post'
urlpatterns = [
    path('create_post/', PostCreateView.as_view(), name='post-create'),
    path("post/<slug:slug>/detail/", PostDetailView.as_view(), name="post-detail"),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("list_post/", PostListView.as_view(), name="post-list"),
    path("user_list_post/", UserPostListView.as_view(), name="user-post-list"),
]
