from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.WelcomeView.as_view() , name='welcome'),
    path('login', LoginView.as_view() , name="weblogin" )
]