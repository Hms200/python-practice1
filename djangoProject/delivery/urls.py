from django.urls import path
from delivery import views

app_name = 'delivery'

urlpatterns = [
    path('orders/', views.order_list, name='order_list')
]