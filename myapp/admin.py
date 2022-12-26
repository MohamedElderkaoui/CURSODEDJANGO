from django.contrib import admin
from .models import project, task

# Register your models here.

@admin.register(project)
class projectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
     
@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'project')
    list_per_page = 25