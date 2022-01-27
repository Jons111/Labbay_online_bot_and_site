from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi
class Menu(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Product(models.Model):
    nomi = models.CharField(max_length =30)
    narxi = models.IntegerField()
    tur  = models.ForeignKey(Type,on_delete=models.CASCADE)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)


class Anketa(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.IntegerField()
    tel = models.CharField(max_length=20)
    jins = models.CharField(max_length=20)
    shaxar = models.CharField(max_length=20)
    username = models.CharField(max_length=20)

class Sotib_olingan_maxsulotlar(models.Model):
    nomi = models.CharField(max_length =30)
    narxi = models.IntegerField()
    miqdori = models.IntegerField()
    tur  = models.CharField(max_length =30)
    username = models.CharField(max_length=30)

