from django.contrib import admin

from .models import Paquete


class PaqueteAdmin(admin.ModelAdmin):
    model = Paquete
admin.site.register(Paquete, PaqueteAdmin)