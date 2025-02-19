from django.shortcuts import render
from cars.models import Car
#from django.http import HttpResponse
# Create your views here.

def cars(request):
    carro = Car.objects.filter(factory_year__gte=2009)

    return render(
        request, 
        'cars.html',
        {'cars': carro}
    )