# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blogs.models import User, Blog

from django.contrib import admin

# Register your models here.

admin.site.register(Blog)
admin.site.register(User)
