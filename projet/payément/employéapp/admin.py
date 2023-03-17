from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
#admin.site.register(Coures)
@admin.register(Employe)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom','genre', 'status', 'service', 'contrat')
    ordering = ('nom', )
    search_fields = ('nom', )
@admin.register(Adresse)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email','quartier', 'ville', )
    ordering = ('email', )
    search_fields = ('email', )
@admin.register(Recu)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('numero', 'date', 'montant', 'reste', )
    ordering = ('numero', )
    search_fields = ('numero', )
@admin.register(Banque)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom','montant', 'validation', )
    ordering = ('nom', )
    search_fields = ('nom', )
