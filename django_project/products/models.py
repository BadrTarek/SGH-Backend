from django.db import models
from django_countries.fields import CountryField
from django.utils.crypto import get_random_string
from users.models import User
from django.utils.safestring import mark_safe
# from automated_control.fuzzy_logic_models.configurations import TIME_BETWEEN_FUZZY_ACTIONS
from datetime import timedelta
# from monitoring.models import Sensor
# from controlling.models import Actuator

TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=10)

class Product(models.Model):
    password = models.CharField(max_length=10, default=get_random_string(length=7))

    country = CountryField()

    is_active = models.BooleanField(default=True)

    image = models.ImageField(upload_to="ProductUploads/")

    user = models.ForeignKey(User, related_name='user_id', blank=True, null=True, on_delete=models.CASCADE)

    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    # sensors = models.ManyToManyField(Sensor, related_name="product_sensors", through='ProductSensor')
    # actuators = models.ManyToManyField(Actuator, related_name="product_actuators", through='ProductActuator')

    token = models.TextField(max_length=500, null=True, blank=True)

    # session_id = models.TextField(max_length=500, null=True, blank=True)

    automated_control = models.BooleanField(default=True)

    time_between_automated_action = models.TimeField(default=TIME_BETWEEN_FUZZY_ACTIONS)

    def __str__(self):
        return str(self.id)

    # Helper functions

    def get_user_products(user: User):
        return Product.objects.filter(user=user, is_active=True)

    def get_product(product_id: int, password: str):
        return Product.objects.filter(pk=product_id, password=password, is_active=True).last()




