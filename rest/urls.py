from django.urls import path
from .views import *

urlpatterns = [
    path('', translate, name='translate'),
]
