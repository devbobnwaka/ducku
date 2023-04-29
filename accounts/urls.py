from django.urls import path
from .views import (Register, Login, Logout, RegisterMember)

app_name='accounts'
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('register_member/', RegisterMember.as_view(), name='register_member'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
