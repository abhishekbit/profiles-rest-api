from urllib.parse import urlparse
from django.urls import path

from profies_api import views

urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()),
]