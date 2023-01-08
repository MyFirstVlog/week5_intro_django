from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,  name='index'),
    path('city/<int:_id>', views.get_city, name='city'),
    path('city/<int:_id>/create_new_comment', views.create_new_comment, name='create_new_comment') #adicionamos la vista que como tal es el endpoint que procesara la informacion
]
