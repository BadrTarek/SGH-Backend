from django.contrib import admin

# Register your models here.

from .models import Sensor
# Register your models here.


class SensorAdmin (admin.ModelAdmin):
    list_display = ('id','image_tag','messure',)
    list_display_links = ('image_tag','id','messure',)
    writeonly_fields = ('image_tag',)
    list_filter = ('created_at',)


admin.site.register(Sensor , SensorAdmin)
