from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import bookedevent
from . models import Event
from . models import decelements
from . forms import EventForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

# views for available events list

def eventlist(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)

    events_list=Event.objects.order_by('priority')
    events_paginator=Paginator(events_list,3)
    events_list=events_paginator.get_page(page)
    context={'events': events_list}
    return render(request,'eventlayout.html', context)

def decelementlist(request):
    decelement_list=decelements.objects.all()
    deccontext={'decelements': decelement_list}
    return render(request,'eventlayout.html', deccontext)

# views for details about event

def eventdetails(request,pk):
    event=Event.objects.get(pk=pk)
    context={'event':event}
    return render(request,'eventdetails.html',context)

#views of rendering html page
def main(request):
    return render(request,'main.html')

def signup(request):
    return render(request,'signup.html')

# views of showing event page
def events(request):

    eventdetails={'events': [
    {
        'title':"Marriage",
        'eventdate': "12/04/2024",
        'status': True,
        'image' : 'marriage.jpg',
    },

    {
        'title':"House Warming",
        'eventdate': "24/07/2024",
        'eventtheme': 'elite',
        'status': False,
        'image' : 'housewarming.jpg',
    },
    {
        'title':"Birthday party",
        'eventdate': "01/02/2024",
        'eventtheme': 'Rock',
        'status': True,
        'image' : 'birthdayparty.jpg',
    },
    {
        'title':"Bride to Be",
        'eventdate': "30/09/2024",
        'eventtheme': 'delight',
        'status': True,
        'image' : 'bridetobe.jpg',
    },
    {
        'title':"Corporate Event",
        'eventdate': "19/05/2024",
        'eventtheme': 'rock',
        'status': False,
        'image' : 'corporateevent.jpg',
    }
    ]}
    return render(request,'event.html', eventdetails)


def createevent(request):
    eventform=EventForm()
    if request.POST:
        eventtype=request.POST.get('eventtype')
        audiencecount=request.POST.get('audiencecount')
        eventdate=request.POST.get('eventdate')
        bookedevent_obj=bookedevent(eventtype=eventtype,audiencecount=audiencecount,eventdate=eventdate)
        bookedevent_obj.save()

    return render(request,'createevent.html',{'eventform':eventform})


def listevent(request):
    bookedevent_set=bookedevent.objects.all()

    return render(request,'eventlist.html', {'bookedevent':bookedevent_set})

def editevent(request):
    return render(request,'editevent.html')




