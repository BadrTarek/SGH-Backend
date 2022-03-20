from django.contrib import admin

from Apps.Greenhouses.models import Greenhouse , GreenhousePlant , GreenhouseActustor , GreenhouseSensor


class GreenhouseAdmin (admin.ModelAdmin):
    list_display = ('id','is_active','country','user')
    list_filter = ('created_at','country','is_active')
    
    

admin.site.register(Greenhouse , GreenhouseAdmin)
admin.site.register(GreenhouseSensor )
admin.site.register(GreenhouseActustor )
admin.site.register(GreenhousePlant)
# Register your models here.
