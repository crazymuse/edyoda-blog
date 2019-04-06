# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django import forms

# Create your models here.
class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=9,blank=True)

    def __str__(self):
        return self.value

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=9,blank=True)
    def __str__(self):
        return self.value

class User(models.Model):
    username = models.CharField(max_length=50, blank=False,unique=True)
    password = models.CharField(max_length=192, blank=False)
    short_desc = models.TextField(blank=True, max_length=150)
    created_on = models.DateTimeField('created on')
    status = models.CharField(max_length=9,blank=True)
    last_logged_in = models.DateTimeField('last logged in',default=timezone.now()) 
    #full_name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=50,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    body = models.TextField(blank=True,max_length=1500)
    status = models.CharField(max_length=9,blank=True)
    first_published = models.DateTimeField("first published")
    last_edited = models.DateTimeField("last edited")
    def __str__(self):
        return self.title



