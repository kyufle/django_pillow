from django.contrib import admin
from django.utils.html import format_html
from .models import Llibre, Usuari

class LlibreAdmin(admin.ModelAdmin):
    list_display = ('titol', 'autor', 'data_edicio')
    readonly_fields = ('vista_previa_imatge',)
    fields = ('titol', 'autor', 'imatge', 'vista_previa_imatge')
    
    def vista_previa_imatge(self, obj):
        if obj.imatge:
            return format_html('<img src="{}" width="200" style="object-fit: contain;" />', obj.imatge.url)
        return "No hi ha imatge"
    
    vista_previa_imatge.short_description = 'Previsualització'

admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Usuari)