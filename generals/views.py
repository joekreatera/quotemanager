from django.shortcuts import render
from django.views import View
# Create your views here.



def WelcomeView(View):

    def get(self, request):
        return render(request, 'welcome.html')