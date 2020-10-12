from django.contrib import admin

from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display=['todo','is_completed']
    

admin.site.register(Todo,TodoAdmin)
# Register your models here.
