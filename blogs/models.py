# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, blank=False,unique=True)
    password = models.CharField(max_length=12, blank=False)
    short_desc = models.TextField(blank=True, max_length=150)
    created_on = models.DateTimeField('created on')
    full_name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=50,blank=False)
    user = models.ForeignKey(User)
    body = models.TextField(blank=True,max_length=1500)
    status = models.CharField(max_length=10,blank=False)
    first_published = models.DateTimeField("first published")
    last_edited = models.DateTimeField("last edited") 

    def __str__(self):
        return self.title
