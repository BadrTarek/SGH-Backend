from turtle import position
from django.db import models
from django.utils.safestring import mark_safe


class Sensor(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    messure = models.CharField(max_length=150 , null= True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=600 , null=True , blank=True)
    image = models.ImageField(upload_to="HardwareUploads/")
    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    
class SensorValues(models.Model):
    value = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensor , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    greenhouse = models.ForeignKey("Greenhouses.Greenhouse" , related_name="greenhouse_sensor_values" ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.value


class Actuator(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    action = models.CharField(max_length=150 , null= True , blank=True)
    description = models.TextField(max_length=600 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="HardwareUploads/")
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" />')
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    def __str__(self):
        return self.name


class ActuatorsAction(models.Model):
    value = models.CharField(max_length=50)
    duration = models.CharField(null = True , blank=True , max_length=50)
    actuator = models.ForeignKey(Actuator , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    greenhouse = models.ForeignKey("Greenhouses.Greenhouse" , on_delete=models.CASCADE)

    def __str__(self):
        return self.value
    



