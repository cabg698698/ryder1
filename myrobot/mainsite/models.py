from django.db import models

# Create your models here.
class Location(models.Model):
    box_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    lng_lat = models.CharField(max_length=50)
    entry_method = models.CharField(max_length=200)
    source_type = models.CharField(max_length=50)
    remark = models.CharField(max_length=400)