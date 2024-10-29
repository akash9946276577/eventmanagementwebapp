from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import bookedevent
from . forms import EventForm

# Create your views here.
def index(request):
    return render(request,'index.html')

# views for available events list

def eventlist(request):
    return render(request,'eventlayout.html')

# views for details about event

def eventdetails(request):
    return render(request,'eventdetails.html')

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




