from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale

from .forms import SalesSearchForm
import pandas as pd


# Create your views here.

def home_view(request):
    sales_df=None
    title = "Sales Home"
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        print(date_to, date_from, chart_type)

        qs=Sale.objects.filter(created_at__date__lte=date_from,created_at__date__gte=date_to)
        obj=Sale.objects.get(id=4)
        if len(qs)>0:
            sales_df = pd.DataFrame(qs.values())
            sales_df=sales_df.to_html()
            print(sales_df)

        else:
            print('no date')







    context = {
        'title': title,
        'form': form,
        'sales_df':sales_df,
    }
    return render(request, 'sales/home.html', context)


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
