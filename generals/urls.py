from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.WelcomeView.as_view() , name='welcome'),
    path('login', LoginView.as_view(template_name="login.html" , next_page="welcome") , name="web_login" ),
    path('logout', views.Logout.as_view() , name='web_logout'),
]