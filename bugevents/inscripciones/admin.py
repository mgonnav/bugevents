from django.contrib import admin

from .models import Paquete, Promocion


class PaqueteAdmin(admin.ModelAdmin):
    model = Paquete
admin.site.register(Paquete, PaqueteAdmin)

class PromocionAdmin(admin.ModelAdmin):
    model=Promocion
admin.site.register(Promocion, PromocionAdmin)