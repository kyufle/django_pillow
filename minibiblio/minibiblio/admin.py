from django.contrib import admin
from django.utils.html import format_html
from .models import Llibre, ImatgeLlibre, Usuari

class ImatgeLlibreInline(admin.TabularInline):
    model = ImatgeLlibre
    extra = 1
    fields = ('imatge', 'preview', 'descripcio')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj and obj.imatge:
            return format_html('<img src="{}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 4px;" />', obj.imatge.url)
        return "Sense imatge"
    
    preview.short_description = 'Miniatura'

class LlibreAdmin(admin.ModelAdmin):
    list_display = ('titol', 'autor', 'data_edicio')
    inlines = [ImatgeLlibreInline]
    readonly_fields = ('portada_actual', 'ver_galeria_completa')
    
    fields = ('titol', 'autor', 'resum', 'data_edicio', 'imatge', 'portada_actual', 'ver_galeria_completa')
    
    def portada_actual(self, obj):
        if obj and obj.imatge:
            return format_html('<img src="{}" style="width: 150px; border: 1px solid #ccc; border-radius: 8px;" />', obj.imatge.url)
        return "No hi ha portada"

    def ver_galeria_completa(self, obj):
        if not obj or not obj.pk:
            return "Guarda el llibre per veure la galeria."

        html = '<div style="display: flex; flex-wrap: wrap; gap: 10px; padding: 15px; border-radius: 8px;">'
        if obj.imatge:
            html += format_html(
                '<div style="text-align: center;">'
                '<p><b>Portada</b></p>'
                '<img src="{}" width="150" style="border: 2px solid #79aec8; border-radius: 4px;" />'
                '</div>', 
                obj.imatge.url
            )

        for img_obj in obj.galeria.all():
            if img_obj.imatge:
                html += format_html(
                    '<div style="text-align: center;">'
                    '<p style="font-size: 10px; color: #666;">{}</p>'
                    '<img src="{}" width="180" height="180" style="object-fit: cover; border-radius: 4px; border: 1px solid #ccc;" />'
                    '</div>', 
                    img_obj.descripcio or "Galeria",
                    img_obj.imatge.url
                )
        
        html += '</div>'
        return format_html(html)
    
    portada_actual.short_description = 'Vista prèvia portada'
    ver_galeria_completa.short_description = 'Àlbum de fotos'

admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Usuari)