from django.db import models

class Plant(models.Model):
    type =  models.CharField(max_length=120)
    image = models.ImageField(upload_to="PlantsUploads/")
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.type
    

