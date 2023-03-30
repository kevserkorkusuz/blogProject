from django.contrib import admin
from.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('user', 'name', 'surname', 'created_at', 'id')
    list_display_links=('user','name')
    search_fields=('name', )
    date_hierarchy='created_at'
    list_filter= ('user', 'name')
    # list_editable = ('surname',)
    list_per_page= 15
    readonly_fields = ('id', 'created_at', 'slug')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
