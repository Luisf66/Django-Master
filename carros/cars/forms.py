from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_yaer = forms.IntegerField()
    value = forms.FloatField()
    plate = forms.CharField(max_length=10)
    photo = forms.ImageField()