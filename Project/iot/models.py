from django.db import models
from django_countries.fields import CountryField
from django.utils.crypto import get_random_string
from users.models import User
from django.utils.safestring import mark_safe
# from automated_control.fuzzy_logic_models.configurations import TIME_BETWEEN_FUZZY_ACTIONS
from datetime import timedelta
TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=10)

class Sensor(models.Model):
    name = models.CharField(max_length=120)
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
    
    
    # Helper functions
    def get_sensor(id:int):
        return Sensor.objects.filter(pk=id).last()

class Actuator(models.Model):
    name = models.CharField(max_length=120)
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
    
    # Helper functions
    def get_actuator(id:int):
        return Actuator.objects.filter(pk=id).last()
    

class Product(models.Model):

    password = models.CharField(max_length=10, default=get_random_string(length=7))

    country = CountryField()

    is_active = models.BooleanField(default=True)

    image = models.ImageField(upload_to="ProductUploads/")

    user = models.ForeignKey(User, related_name='user_id', blank=True, null=True, on_delete=models.CASCADE)

    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    sensors = models.ManyToManyField(Sensor,  related_name="product_sensors", through='ProductSensor')
    actuators = models.ManyToManyField(Actuator, related_name="product_actuators", through='ProductActuator')

    token = models.TextField(max_length=500, null=True, blank=True)

    automated_control = models.BooleanField(default=True)
    
    time_between_automated_action = models.TimeField(default  = TIME_BETWEEN_FUZZY_ACTIONS)
    
    def __str__(self):
        return str(self.id)
    
    # Helper functions
    
    def get_user_products(user:User):
        return Product.objects.filter(user = user, is_active=True)
    
    def get_product(product_id:int, password:str):
        return Product.objects.filter(pk=product_id , password = password, is_active=True).last()
    
    
class ProductSensor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True, blank=True)
    
    # Helper functions
    def get_product_sensors(product:Product):
        return ProductSensor.objects.filter(product = product)

class ProductActuator(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True, blank=True)
    
    # Helper functions
    def get_product_actuators(product:Product):
        return ProductActuator.objects.filter(product = product)
    



class SensorValues(models.Model):
    value = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensor , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product , related_name="product_sensor_values" ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.value
    
    # Helper functions
    def get_all_sensor_values(product:Product , sensor:Sensor):
        return SensorValues.objects.filter(product = product , sensor = sensor)
    
    def get_last_sensor_values(product:Product , sensor:Sensor):
        try:
            return SensorValues.objects.filter(product = product , sensor = sensor).order_by('-id')[0]
        except :
            pass
        return SensorValues.objects.filter(product = product , sensor = sensor).order_by('-id')
    
    def get_before_last_sensor_values(product:Product , sensor:Sensor):
        try:
            return SensorValues.objects.filter(product = product , sensor = sensor).order_by('-id')[1]
        except :
            pass
        return SensorValues.objects.filter(product = product , sensor = sensor).order_by('-id')

class ActuatorsAction(models.Model):
    value = models.CharField(max_length=50)
    duration = models.CharField(null = True , blank=True , max_length=50)
    actuator = models.ForeignKey(Actuator , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    is_automated_action = models.BooleanField(default=False)

    def __str__(self):
        return self.value
    
    # Helper functions
    def get_all_actuator_actions(product:Product , actuator:Actuator):
        return ActuatorsAction.objects.filter(product = product , actuator = actuator)
    
    def get_last_actuator_actions(product:Product , actuator:Actuator):
        try:
            return ActuatorsAction.objects.filter(product = product , actuator = actuator).order_by('-id')[0]
        except :
            pass
        return ActuatorsAction.objects.filter(product = product , actuator = actuator).order_by('-id')
    
    def get_last_automated_actions(product:Product , actuator:Actuator):
        try:
            return ActuatorsAction.objects.filter(product = product , actuator = actuator,is_automated_action=True ).order_by('-id')[0]
        except :
            pass
        return ActuatorsAction.objects.filter(product = product , actuator = actuator,is_automated_action=True).order_by('-id')



    
    def get_last_automated_actions(product:Product , actuator:Actuator):
        print(actuator)
        print(product)
        try:
            return ActuatorsAction.objects.filter(product = product , is_automated_action = True , actuator = actuator).order_by('-id')[0]
        except :
            pass
        return ActuatorsAction.objects.filter(product = product , is_automated_action = True , actuator = actuator).order_by('-id')


