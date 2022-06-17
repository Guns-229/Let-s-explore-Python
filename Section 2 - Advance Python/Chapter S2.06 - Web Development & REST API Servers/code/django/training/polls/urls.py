#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:57:08 2018

@author: mayank
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
