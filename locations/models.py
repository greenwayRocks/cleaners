from django.db import models
from datetime import datetime
from neatfreaks.models import Cleaner

class Location(models.Model):
    cleaner = models.ForeignKey(Cleaner, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.title
