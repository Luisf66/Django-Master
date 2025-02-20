from django.shortcuts import render
from cars.models import Car
#from django.http import HttpResponse
# Create your views here.

def cars(request):
    carro = Car.objects.all().order_by('model')

    search = request.GET.get('search')

    if search:
        carro = carro.filter(model__icontains = search)
    return render(
        request, 
        'cars.html',
        {'cars': carro}
    )