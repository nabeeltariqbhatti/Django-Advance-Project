from django.urls import path

from . import views

app_name = "Sales"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sales/', views.SalesListView.as_view(), name='list'),
    path('sales/<int:pk>/', views.SalesDetailView.as_view(), name='detail')
]
