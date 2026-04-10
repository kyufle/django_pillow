from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Llibre, ImatgeLlibre, Usuari

# --- CONFIGURACIÓN DE USUARIO ---

class UsuariAdmin(UserAdmin):
    # Añadimos el campo auth_token a los fieldsets existentes de Django UserAdmin
    fieldsets = UserAdmin.fieldsets + (
        ("Altres dades (API auth)", {
            'fields': ('auth_token',),
        }),
    )
    readonly_fields = ["auth_token",]

# --- CONFIGURACIÓN DE IMÁGENES (INLINE) ---

class ImatgeLlibreInline(admin.TabularInline):
    model = ImatgeLlibre
    extra = 1
    fields = ('imatge', 'preview_inline', 'descripcio')
    readonly_fields = ('preview_inline',)

    def preview_inline(self, obj):
        if obj and obj.imatge:
            return format_html('<img src="{}" style="height: 50px; border-radius: 4px;" />', obj.imatge.url)
        return ""
    preview_inline.short_description = 'Vista prèvia'

# --- CONFIGURACIÓN DE LIBROS ---

class LlibreAdmin(admin.ModelAdmin):
    list_display = ('titol', 'mini_galeria_llistat')
    inlines = [ImatgeLlibreInline]
    readonly_fields = ('ver_galeria_completa',)
    fields = ('titol', 'autor', 'resum', 'data_edicio', 'imatge', 'ver_galeria_completa')

    def mini_galeria_llistat(self, obj):
        html = '<div style="display: flex; gap: 4px;">'
        if obj.imatge:
            html += format_html('<img src="{}" style="width: 200px; height: 200px; object-fit: cover; border-radius: 3px; border: 1px solid #79aec8;" />', obj.imatge.url)
        
        for img_obj in obj.galeria.all()[:3]:
            html += format_html('<img src="{}" style="width: 200px; height: 200px; object-fit: cover; border-radius: 3px; border: 1px solid #ccc;" />', img_obj.imatge.url)
        
        html += '</div>'
        return format_html(html)
    mini_galeria_llistat.short_description = 'Galeria'

    def ver_galeria_completa(self, obj):
        if not obj or not obj.pk:
            return "Guarda el llibre per veure la galeria completa."

        html = '<div style="display: flex; flex-wrap: wrap; gap: 10px; background: #f8f8f8; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">'
        
        if obj.imatge:
            html += format_html(
                '<div style="text-align: center;">'
                '<p><b>Portada</b></p>'
                '<img src="{}" width="180" style="object-fit: cover; border: 2px solid #79aec8; border-radius: 4px;" />'
                '</div>', 
                obj.imatge.url
            )
        
        imagenes_galeria = obj.galeria.all()
        if imagenes_galeria.exists():
            for img_obj in imagenes_galeria:
                if img_obj.imatge:
                    html += format_html(
                        '<div style="text-align: center;">'
                        '<p style="font-size: 10px; color: #666;">Galería</p>'
                        '<img src="{}" width="200" height="200" style="object-fit: cover; border-radius: 4px; border: 1px solid #ccc;" />'
                        '</div>', 
                        img_obj.imatge.url
                    )
        else:
            if not obj.imatge:
                return "Encara no hi ha cap imatge pujada."
                
        html += '</div>'
        return format_html(html)
    
    ver_galeria_completa.short_description = 'Àlbum de fotos del llibre'

# --- REGISTRO DE MODELOS ---

admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Usuari, UsuariAdmin)