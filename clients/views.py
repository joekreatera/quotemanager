from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse
# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Client
from .forms import ClientForm

class TestClientsView(View):

    def get(self, request):
        #return HttpResponse("Hello there!")
        print(request.GET)
        return render(request, "index.html", {"data":"hello joe" , "data2":"second data"})
    

class ListClientsView(ListView):
    model = Client 
    context_object_name = "clients"

class DetailClientsView(DetailView):
    model = Client

class NewClientView(View):

    def get(self, request):
        form = ClientForm()
        return render(request, "form_template.html", {"form":form})

    def post(self, request):
        form  = ClientForm(request.POST)

        if( form.is_valid()):
            form.save()
            return redirect('list')
        
        return render(request, "form_template.html", {"form":form})
