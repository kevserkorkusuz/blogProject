from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =  ('owner', 'title', 'created_at', 'isPublish')
    list_editable=('isPublish',)
    search_fields =('title',)
    list_filter=('owner', 'isPublish')
    readonly_fields=('id', 'created_at', 'slug')
    date_hierarchy='created_at'
    list_per_page=10

admin.site.register(Post, PostAdmin)