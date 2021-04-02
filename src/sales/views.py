from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale


# Create your views here.

def home_view(request):
    context = "Hello This is the first Demo text"
    return render(request, 'sales/home.html', {'demo': context})


class SalesListView(ListView):
    model = Sale
    template_name = "sales/main.html"
    context_object_name = 'qs'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

    def sale_list_view(request):
        qs = Sale.object.all();
        return render(request, '/main.html', {qs: qs})

    def sale_detail_view(request, **kwargs):
        pk = kwargs.get('pk')
        obj = Sale.objects.get(pk=pk)
        return render(request, 'sales/detail.html',

                      {'object': obj})
