from django.contrib import admin

from chronicle.models import Event, Chronicle

admin.site.register(Chronicle)
admin.site.register(Event)
