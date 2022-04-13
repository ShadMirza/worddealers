from cgitb import enable
from turtle import heading
from os import link
from django.db import models

# Create your models here.

class Index(models.Model):
    tagline_1 = models.TextField(max_length=100)
    tagline_2 = models.TextField(max_length=100)
    main_heading = models.TextField(max_length=100, null= True)
    about = models.TextField(max_length=200, null= True)
    team_heading = models.TextField(max_length=200, null= True)
    services_heading = models.TextField(max_length=200, null= True)
    portfolio = models.TextField(max_length=200, null= True)
    contact_description = models.TextField(max_length=200, null= True)
    subscribe_heading = models.TextField(max_length=100, null= True)
    address = models.CharField(max_length=150, null= True)
    number = models.CharField(max_length=150, null= True)
    facebook_link = models.URLField(max_length=150, null= True, blank=True)
    twitter_link = models.URLField(max_length=150, null= True, blank=True)
    linkedin_link = models.URLField(max_length=150, null= True, blank=True)
    instagram_link = models.URLField(max_length=150, null= True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='clients', null=True, blank=True)

    def __str__(self):
        return str(self.name)
