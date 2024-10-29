from django.contrib import admin
from . models import bookedevent, Event, decelements

# Register your models here.
admin.site.register(bookedevent)
admin.site.register(Event)
admin.site.register(decelements)