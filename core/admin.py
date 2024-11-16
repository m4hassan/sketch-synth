from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Unregister Group model

admin.site.unregister(Group)
admin.site.register(Creations)