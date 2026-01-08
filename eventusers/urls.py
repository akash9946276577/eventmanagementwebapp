from django.urls import path
from . import views

urlpatterns = [
    path('account/',views.show_account,name='account'),
    path('login/', views.show_login, name='login')
]