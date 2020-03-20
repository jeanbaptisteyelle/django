from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('image_view','nom','prenom', 'description', 'signature', 'vidéo_url'
    )
    list_filter = ('status',)

    search_field = ('nom',)

    date_hierachy = "date_add"

    list_display_links = ['prenom']

    list_per_page = 10

    fieldsets = [
        ('Presentation',{ 'fields':['nom','prenom']}),
        ('standard',{ 'fields':['status']})
    ]

    def image_view(self,obj):
        
        return mark_safe("<img src='{url}' width= '100px', height= '50px'>".format(url=obj.image.url))


def _register(model, Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Presentation, PresentationAdmin)