# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Species(models.Model):
    Scientific_Name = models.CharField(max_length=200)
    Kingdom_Name = models.CharField(max_length=200)
    Phylum_Name = models.CharField(max_length=200)
    Class_Name = models.CharField(max_length=200)
    Order_Name = models.CharField(max_length=200)
    Family_Name = models.CharField(max_length=200)
    Subfamily_Name = models.CharField(max_length=200)
    Genus_Name = models.CharField(max_length=200)



    def __str__(self):
        return self.Scientific_Name

class Taxonomic_Group(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
