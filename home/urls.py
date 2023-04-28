from django.urls import path
from .views import (Index, AboutUs, Home)

app_name='home'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', AboutUs.as_view(), name='about'),
    path('home/', Home.as_view(), name='home'),
]
