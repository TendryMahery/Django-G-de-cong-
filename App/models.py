from typing import ValuesView
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value

# Create your models here.
class Autorisation(models.Model):
    TYPE = (('Approuvé','Approuvé'),
           ('Refusé','Refusé'))
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=50,null=True)
    ma = models.IntegerField()
    cadre = models.CharField(max_length=50,null=True)
    departement=models.CharField(max_length=50,null=True)
    typeconge=models.CharField(max_length=50,null=True)  
    datedebut = models.DateField(null=True)
    datefin = models.DateField(null=True)
    dure = models.IntegerField(null=True)
    notification = models.CharField(max_length=50,null=True,choices=TYPE)
    def __str__(self):
        return self.nom
class Presence(models.Model):
    userp = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.nom
class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    userC = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Actualite(models.Model):
    titre = models.CharField(max_length=50)
    paragraphe = models.TextField(max_length=100)
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.titre

class Personnel(models.Model):
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)
    imagem = models.ImageField(upload_to='image')
    departement =models.CharField(max_length=50,null=True)
    post =models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.nom

class Ministre(models.Model):
    mot = models.TextField(max_length=500)
    imageministre = models.ImageField(upload_to='image')

