# join_community/urls.py
from django.urls import path
from .views import signup, subscribe, success

app_name = 'join_community'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('subscribe/', subscribe, name='subscribe'),
    path('success/', success, name='success'),
]
