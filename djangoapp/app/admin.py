from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Novidade, PortalBusca, Assunto, Especialista, AvisoPorEmail

# Classe que gerencia a interface de admin do Django

admin.site.site_header = "Projeto robo covid ADMIN"

class portalBuscaAdmin(admin.ModelAdmin):
	pass
	#fields = ('*')

class NovidadeAdmin(admin.ModelAdmin):
	#fields = ('titulo', ...)
	list_display = ('titulo', 'dataPrimeiroAcesso')
	list_filter = ('dataPrimeiroAcesso',)

admin.site.register(Novidade, NovidadeAdmin)
admin.site.register(PortalBusca, portalBuscaAdmin)

admin.site.unregister(Group)

