from django.forms import ModelForm
from . models import bookedevent

class EventForm(ModelForm):
    class Meta:
        model=bookedevent
        fields='__all__'