# contact/urls.py
from django.urls import path
from .views import contact_view, success_page_view

urlpatterns = [
    path('contact/', contact_view, name='contact_view'),
    path('success/', success_page_view, name='success_page'),
]

