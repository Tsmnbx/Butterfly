# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Species

# Create your views here.

def index(request):
    #return HttpResponse("Hello, Welcome to the Butterfly Pavilion!")
    Species_list= Species.objects.order_by('Scientific_Name')
    output = ', '.join([Species.Scientific_Name for Species in Species_list])
    return HttpResponse(output)

def species_id(request, Scientific_Name):
    return HttpResponse("This is the species %s" % Scientific_Name)
