from django.urls import path
from .views import index, signin, signup

urlpatterns = [
    path('', index),
    path('signin/', signin),
    path('signup/', signup)
]