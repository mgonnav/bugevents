from django.contrib import admin

from .models import Paquete, Promocion
from .forms import PaqueteForm, PromocionForm


class PaqueteAdmin(admin.ModelAdmin):
    model = Paquete
    form = PaqueteForm
admin.site.register(Paquete, PaqueteAdmin)


class PromocionAdmin(admin.ModelAdmin):
    model = Promocion
    form = PromocionForm
admin.site.register(Promocion, PromocionAdmin)