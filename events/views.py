from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#views of rendering html page
def main(request):
    return render(request,'main.html')

# views of showing event page
def events(request):

    eventdetails={'events': [
    {
        'title':"Marrage",
        'eventdate': "12/04/2024",
        'status': True
    },

    {
        'title':"House Warming",
        'eventdate': "24/07/2024",
        'eventtheme': 'elite',
        'status': False
    },
    {
        'title':"Birthday party",
        'eventdate': "01/02/2024",
        'eventtheme': 'Rock',
        'status': True
    },
    {
        'title':"Bride to Be",
        'eventdate': "30/09/2024",
        'eventtheme': 'delight',
        'status': True
    },
    {
        'title':"Corporate Event",
        'eventdate': "19/05/2024",
        'eventtheme': 'rock',
        'status': False
    }
    ]}
    return render(request,'event.html', eventdetails)

