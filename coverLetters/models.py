from django.db import models

# Create your models here.
class CoverLetter(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    yoe = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    passion = models.CharField(max_length=100)
    products = models.CharField(max_length=100)