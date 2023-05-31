from django.urls import path
from landing.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]