from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .forms import QuoteForm
from .models import Quote
# Create your views here.


class NewQuoteView(View):

    def get(self, request):
        form = QuoteForm()
        return render(request, "form_template.html", {"form":form})

    def post(self, request):
        form  = QuoteForm(request.POST)

        if( form.is_valid()):
            form.save()
            return redirect('list')
        
        return render(request, "form_template.html", {"form":form})
    

class EditQuoteView(View):

    def get(self, request, pk):
        instance = get_object_or_404(Quote, id=pk)
        form = QuoteForm(instance = instance)
        return render(request, "form_template.html", {"form":form})

    def post(self, request , pk):
        instance = get_object_or_404(Quote, id=pk)
        form  = QuoteForm(request.POST , instance = instance)

        if( form.is_valid()):
            form.save()
            return redirect('list')
        
        return render(request, "form_template.html", {"form":form})
