from django.contrib import admin

from .models import Sensor
from .models import Actuator
# Register your models here.


class SensorAdmin (admin.ModelAdmin):
    list_display = ('id','image_tag','messure','price')
    list_display_links = ('image_tag','id','messure',)
    writeonly_fields = ('image_tag',)
    list_filter = ('price','created_at')

class ActuatorAdmin (admin.ModelAdmin):
    list_display = ('id','image_tag','action','price')
    list_display_links = ('image_tag','id','action',)
    writeonly_fields = ('image_tag',)
    list_filter = ('price','created_at')

admin.site.register(Sensor , SensorAdmin)
admin.site.register(Actuator ,ActuatorAdmin)
