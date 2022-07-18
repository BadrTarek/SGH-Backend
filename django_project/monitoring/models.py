from django.db import models
from django.utils.safestring import mark_safe
from products.models import Product

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=120)
    messure = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=600, null=True, blank=True)
    image = models.ImageField(upload_to="HardwareUploads/")

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    # Helper functions
    def get_sensor(id: int):
        return Sensor.objects.filter(pk=id).last()

# class ProductSensor(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
#     position = models.CharField(max_length=200, null=True, blank=True)
#
#     # Helper functions
#     def get_product_sensors(product: Product):
#         return ProductSensor.objects.filter(product=product)



class SensorValues(models.Model):
    value = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name="product_sensor_values", on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    # Helper functions
    def get_all_sensor_values(product: Product, sensor: Sensor):
        return SensorValues.objects.filter(product=product, sensor=sensor)

    def get_last_sensor_values(product: Product, sensor: Sensor):
        try:
            return SensorValues.objects.filter(product=product, sensor=sensor).order_by('-id')[0]
        except:
            pass
        return SensorValues.objects.filter(product=product, sensor=sensor).order_by('-id')

    def get_before_last_sensor_values(product: Product, sensor: Sensor):
        try:
            return SensorValues.objects.filter(product=product, sensor=sensor).order_by('-id')[1]
        except:
            pass
        return SensorValues.objects.filter(product=product, sensor=sensor).order_by('-id')



