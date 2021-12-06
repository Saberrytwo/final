from django.contrib import admin

# Register your models here.

from .models import PdDrugs, PdPrescriber, PdPrescribersCredentials, PdStatedata, PdTriple

admin.site.register(PdTriple)
admin.site.register(PdDrugs)
admin.site.register(PdPrescriber)
admin.site.register(PdPrescribersCredentials)
admin.site.register(PdStatedata)
