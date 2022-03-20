from django.db import models
from Apps.GreenhouseApp.models import Greenhouse
# Create your models here.



class WaterComponent(models.Model):
    type =  models.CharField(max_length=120)
    quantity = models.CharField(max_length=10)
    greenhouse = models.ForeignKey(Greenhouse , related_name="greenhosue_id")
    
    
    
class GreenhouseWaterComponent(models.Model):
    pass