from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField()
    model_yaer = models.IntegerField()
    value = models.FloatField()
    plate = models.TextField(max_length=10, null=True, blank=True)
    photo = models.ImageField(upload_to='cars/', null=True, blank=True)

    def __str__(self):
        return self.model