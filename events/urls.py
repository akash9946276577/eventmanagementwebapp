"""
URL configuration for eventmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('createevent/', views.createevent, name='createevent'),
    path('editevent/', views.editevent, name='editevent'),
    path('listevent/', views.listevent, name='listevent'),
    path('loginprompt/',views.main, name='loginpage'),
    path('bookedevents/',views.events, name='events'),
    path('signup/', views.signup, name='signup'),
]
