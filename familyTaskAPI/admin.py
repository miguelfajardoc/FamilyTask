from django.contrib import admin

from .models import User, GeneralTask, Family, Rol, AsignedTask

admin.site.register([User, GeneralTask, Family, Rol, AsignedTask])