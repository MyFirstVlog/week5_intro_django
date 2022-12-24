from django.db import models
from django.utils import timezone

# Nombre de la tabla en la base de datos

class City(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='citiesapp/photos')
  population = models.IntegerField()

  country = models.CharField(max_length=100)

  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Cities'
  
