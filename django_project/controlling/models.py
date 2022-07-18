from django.db import models
from products.models import Product
# Create your models here.

class Actuator(models.Model):
    name = models.CharField(max_length=120)
    action = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="HardwareUploads/")

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    # Helper functions
    def get_actuator(id: int):
        return Actuator.objects.filter(pk=id).last()


# class ProductActuator(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)
#     position = models.CharField(max_length=200, null=True, blank=True)
#
#     # Helper functions
#     def get_product_actuators(product: Product):
#         return ProductActuator.objects.filter(product=product)


class ActuatorsAction(models.Model):
    value = models.CharField(max_length=50)
    duration = models.CharField(null=True, blank=True, max_length=50)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_automated_action = models.BooleanField(default=False)

    def __str__(self):
        return self.value

    # Helper functions
    def get_all_actuator_actions(product: Product, actuator: Actuator):
        return ActuatorsAction.objects.filter(product=product, actuator=actuator).order_by('-id')

    def get_last_actuator_actions(product: Product, actuator: Actuator):
        try:
            return ActuatorsAction.objects.filter(product=product, actuator=actuator).order_by('-id')[0]
        except:
            pass
        return ActuatorsAction.objects.filter(product=product, actuator=actuator).order_by('-id')

    def get_last_automated_actions(product: Product, actuator: Actuator):
        try:
            return \
            ActuatorsAction.objects.filter(product=product, is_automated_action=True, actuator=actuator).order_by(
                '-id')[0]
        except:
            pass
        return ActuatorsAction.objects.filter(product=product, is_automated_action=True, actuator=actuator).order_by(
            '-id')


