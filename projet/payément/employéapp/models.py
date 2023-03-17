from django.db import models

class Adresse(models.Model):
    #matricule = models.CharField(max_length=20,unique=True)
    telephone = models.CharField(max_length=20,blank=True,unique=True)
    email = models.CharField(max_length=250,unique=True)
    quartier = models.CharField(max_length=150)
    ville = models.CharField(max_length=150)
    def __str__(self):
        return self.email
    
class Personne(models.Model):
    Status = (
    ('Ancien', ('ancien')),
    ('Nouveau', ('nouveau')),
    )
    Genre = (
    ('M', ('masculin')),
    ('F', ('feminin')),
    ('Autre', ('autre')),
    )
    nom = models.CharField(max_length=200)
    naissance = models.DateTimeField('date de naisssance')
    genre = models.CharField(max_length=32, choices=Genre)
    status = models.CharField(max_length=32, choices=Status)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="static/photo", default='/static/photo/default.jpg')
    def __str__(self):
        return self.nom

class Employe(Personne):
    Contrat = (
    ('ST', ('stagiaire')),
    ('CDD', ('Contrat à durée déterminé')),
    ('CDI', ('Contrat à durée indéterminé')),
    )
    matricule = models.CharField(max_length=20,unique=True)
    service = models.CharField(max_length=100)
    contrat = models.CharField(max_length=32, choices=Contrat)

    def __str__(self):
        return self.nom




class Recu(models.Model):
    date = models.DateTimeField('date')
    montant = models.CharField(max_length=200)
    reste = models.CharField(max_length=200)
    numero = models.CharField(max_length=120)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)

    def __str__(self):
        return self.montant

class Banque(models.Model):
    nom = models.CharField(max_length=150)
    montant = models.CharField(max_length=200)
    validation = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

