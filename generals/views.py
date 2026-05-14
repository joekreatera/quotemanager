from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login
# Create your views here.



class WelcomeView(View):

    def get(self, request):
        return render(request, 'welcome.html')
    
class Logout(View):

    def get(self, request):
        
        logout(request)
        return redirect('welcome')