from django.contrib import admin

from .models import Product , ProductActuator , ProductSensor



class ProductAdmin (admin.ModelAdmin):
    list_display = ('id','is_active','country','user')
    list_filter = ('created_at','country','is_active')
    
    

# Register your models here.


class ProductAdmin (admin.ModelAdmin):
    list_display = ('id','is_active','country','user')
    list_filter = ('created_at','country','is_active')
    
    

admin.site.register(Product , ProductAdmin)
admin.site.register(ProductSensor )
admin.site.register(ProductActuator )
# Register your models here.


from .models import Sensor
from .models import Actuator
# Register your models here.


class SensorAdmin (admin.ModelAdmin):
    list_display = ('id','image_tag','messure',)
    list_display_links = ('image_tag','id','messure',)
    writeonly_fields = ('image_tag',)
    list_filter = ('created_at',)

class ActuatorAdmin (admin.ModelAdmin):
    list_display = ('id','image_tag','action',)
    list_display_links = ('image_tag','id','action',)
    writeonly_fields = ('image_tag',)
    list_filter = ('created_at',)

admin.site.register(Sensor , SensorAdmin)
admin.site.register(Actuator ,ActuatorAdmin)