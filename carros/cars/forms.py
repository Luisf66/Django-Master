from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_yaer = forms.IntegerField()
    value = forms.FloatField()
    plate = forms.CharField(max_length=10)
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_yaer = self.cleaned_data['model_yaer'],
            value = self.cleaned_data['value'],
            plate = self.cleaned_data['plate'],
            photo = self.cleaned_data['photo']
        )
        car.save()
        return car