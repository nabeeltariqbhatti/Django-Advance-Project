from django.urls import path

from . import views

app_name = "Sales"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('list/', views.SalesListView.as_view(), name='list')
]
