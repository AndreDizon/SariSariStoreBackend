from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.manage_products, name='manage_products'),
    path('customers/<int:customer_id>/debts/', views.get_customer_debt, name='get_customer_debt'),
]
