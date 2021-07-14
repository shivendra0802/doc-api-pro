# from .views import CheckLoginAPI
from .views import CheckLoginAPI
from django.urls import path

urlpatterns = [
    path('check-login', CheckLoginAPI.as_view(), name="check-login")
]
