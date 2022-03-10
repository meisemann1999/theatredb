from django.contrib import admin

from .models import Department, Employee, Event

# Register your models here.

admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(Department)