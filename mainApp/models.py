from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=False)
    name = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=200, blank=True)