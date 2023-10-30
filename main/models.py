from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Formulyar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=500,verbose_name='O`quvchi ismi')
    last_name = models.CharField(max_length=500,verbose_name='O`quvchi Familiyasi')
    sinf = models.CharField(max_length=500,verbose_name='O`quvchi sinfi')
    books = models.TextField(verbose_name='O`quvchi olgan kitoblar')

    def get_absolute_url(self):
        return reverse('home')