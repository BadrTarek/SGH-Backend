from django.contrib import admin 
from .models import Plant
# Register your models here.

class PlantsAdmin (admin.ModelAdmin):
    list_display = ('type','is_supported')
    list_filter = ('is_supported',)
    
admin.site.register(Plant , PlantsAdmin)
# admin.site.register(GreenhousePlants )
