from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm
#from django.http import HttpResponse
# Create your views here.

def cars_view(request):
    carro = Car.objects.all().order_by('model')

    search = request.GET.get('search')

    if search:
        carro = carro.filter(model__icontains = search)
    return render(
        request, 
        'cars.html',
        {'cars': carro}
    )

def new_car_view(request):
    new_car_form = CarForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )
