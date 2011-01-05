from django import forms
from django.contrib import admin
from django.db import models
from generic_content.models import GenericContent
#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3


class GenericContentAdmin(admin.ModelAdmin):
    list_display = ('def_title', 'def_heading', 'def_content')
    list_filter = ['modified']
    search_fields = ['def_title']
    date_hierarchy = 'modified'
    exclude = ('slug',)
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})},}

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(GenericContentAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

    class Media:
        js = ('/js/ckeditor/ckeditor.js', )
        css = {'all': ('/js/ckeditor/contents.css', )}

admin.site.register(GenericContent, GenericContentAdmin)
