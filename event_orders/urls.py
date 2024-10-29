from django.urls import path
from . import views

urlpatterns = [
    path('orderscart/',views.show_orderscart,name='orderscart'),
]