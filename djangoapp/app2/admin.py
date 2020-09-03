from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AvisoPorEmail

class AvisoPorEmailAdmin(admin.ModelAdmin):
	list_display = ('user_alerta', 'assuntoAviso', 'frequencia')

admin.site.register(AvisoPorEmail, AvisoPorEmailAdmin)

