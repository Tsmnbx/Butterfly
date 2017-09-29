# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Species
from .models import Taxonomic_Group

admin.site.register(Species)
admin.site.register(Taxonomic_Group)
