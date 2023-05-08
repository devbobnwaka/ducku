from django.urls import path
from .views import (Section)


app_name='apps'
urlpatterns = [
    path('section/', Section.as_view(), name='section'),
]
