from django.shortcuts import render

from .models import City
# Create your views here.

def index(request):
    cities = City.objects.all()

    print('cities', cities)

    return render(request, 'cities.html', {'cities': cities})

def get_city(request, _id):
    city = City.objects.get(id= _id)

    print('city', city)

    return render(request, 'city.html', {'city': city})