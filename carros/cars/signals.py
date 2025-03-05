from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio
#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

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = f'Carro {instance.model} {instance.brand} {instance.model_yaer}'
        #ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_yaer)
        #instance.bio = ai_bio