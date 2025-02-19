from django.contrib import admin
from cars.models import Car, Brand
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_yaer', 'value')
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)

class Car_BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, Car_BrandAdmin)