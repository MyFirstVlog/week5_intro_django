from django.shortcuts import render, redirect

from .models import City
from .forms import CommentForm
# Create your views here.

def index(request):
    cities = City.objects.all()

    print('cities', cities)

    return render(request, 'cities.html', {'cities': cities})

def get_city(request, _id):
    city = City.objects.get(id= _id)

    comments_form = CommentForm()

    print('city', city)

    return render(request, 'city.html', {'city': city, 'form': comments_form})

def create_new_comment(request, _id): #este es el id de la ciudad
    if(request.method == 'POST'):
        form = CommentForm(request.POST) #dEVUELME INSTANCIA DE COMMENT FORM CON LA INFO DEL REGISTRO

        if form.is_valid():
            new_comment = form.save(commit=False) #Se pone el commit igual a false para forzar el guardado aunque todavia falta por meter user, city
            new_comment.user = request.user
            new_comment.city = City.objects.get(id=_id)

            new_comment.save()

        return redirect('city', id=_id)
    else:
        return redirect('city', id=_id)
