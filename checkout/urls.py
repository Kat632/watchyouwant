from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success,
         name='checkout_success'),
    path('cache_checkout_data/',
         views.cache_checkout_data,
         name='cache_checkout_data'),
    path('is_in_stock/', views.is_in_stock, name='is_in_stock'),
    path('no_sale/', views.no_sale, name='no_sale'),
    path('wh/', webhook, name='webhook'),
]
