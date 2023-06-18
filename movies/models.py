from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Katagori(models.Model):
    name=models.CharField(max_length=50,verbose_name="Katagori Adı")
    def __str__(self):
        return self.name
class Tur(models.Model):
    name=models.CharField(max_length=50,verbose_name="Tür Adı")
    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=100,verbose_name="Film Adı")
    aciklama=models.TextField(max_length=400,verbose_name="Film Açıklması")
    afis=models.FileField(upload_to="afisler",blank=True,null=True, verbose_name="Film Afişi")
    katagori=models.ForeignKey(Katagori,on_delete=models.CASCADE,null=True)
    tur=models.ManyToManyField('Tur',null=True)

    def __str__(self):
        return self.filmismi

class Izlenen(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField('Movies',null=True)
    def __str__(self):
        return self.user.username