#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import admin
from app.models import MyModel

admin.site.register(MyModel)
