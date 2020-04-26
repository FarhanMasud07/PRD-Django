from django.contrib import admin
from .models import notice

# Register your models here.

class notceAdmin(admin.ModelAdmin):
    list_display = ('title','description','date')
    search_fields = ('date',)

admin.site.register(notice,notceAdmin)