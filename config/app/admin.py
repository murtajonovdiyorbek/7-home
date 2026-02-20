from django.contrib import admin

from .models import ServiceCategory, Mechanic, Service

admin.site.register([ServiceCategory, Mechanic, Service])