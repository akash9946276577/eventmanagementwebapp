from django.db import models

# Create your models here.


class bookedevent(models.Model):
    eventtype=models.CharField(max_length=50)
    audiencecount=models.IntegerField()
    eventdate=models.DateField()
