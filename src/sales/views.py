from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale


# Create your views here.

def home_view(request):
    context= "Hello This is the first Demo text"
    return render(request, 'sales/home.html', {'demo':context})

class SalesListView(ListView):

    model =Sale
    template_name="sales/main.html"
    context_object_name = 'qs'
