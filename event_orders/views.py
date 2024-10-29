from django.shortcuts import render

# Create your views here.


def show_orderscart(request):
    return render(request, 'orderscart.html')