from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('signup', views.signup.as_view(), name='signup'),
    path('send_otp', views.send_otp.as_view(), name='send'),
]