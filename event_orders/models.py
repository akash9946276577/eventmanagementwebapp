from django.db import models
from eventusers.models import users
from events.models import Event
# model for cart

class eventcart(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=1
    EVENT_BOOKED=1
    EVENT_PROCESSED=2
    EVENT_DELIVERED=3
    EVENT_REJECTED=4
    STATUS_CHOICE=((EVENT_PROCESSED,'EVENT_PROCESSED'),
                   (EVENT_DELIVERED,'EVENT_DELIVERED'),
                   (EVENT_REJECTED,'EVENT_REJECTED'))
    event_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(users,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=0)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class eventbookeditem(models.Model):
    event=models.ForeignKey(Event,related_name='added_events',on_delete=models.SET_NULL,null=True)
    guestcount=models.IntegerField(default=10)
    owner=models.ForeignKey(eventcart,on_delete=models.CASCADE,related_name='added_events')
