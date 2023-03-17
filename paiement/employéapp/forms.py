from django import forms
from django.forms import ModelForm
from .models import Employe, Adresse, Banque, Recu

class EmployeForm(forms.ModelForm):
	class Meta:
		model = Employe
		fields = [ 'nom', 'naissance', 'genre', 'matricule','status', 'adresse','photo','contrat',]

		labels = {
			'matricule': 'Matricule', 
			'nom': 'Nom et Prenom',       
			'genre': 'Selectionner le genre ', 
			'status': 'Selectionner le status',
			'adresse': 'Selectionner l\'adresse',
			'contrat':'Selectionner le contrat', 
			'photo': 'Selectionner une photo',
			  
		}

		widgets = {
			'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le matricule',}), 
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom et Prenom',}), 
			'naissance': forms.TextInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre',}), 
			'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Status',}),   
			#'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}), 
			'adresse': forms.Select(attrs={'class': 'form-select', 'placeholder': 'adresse',}),
			#'photo': forms.ImageField()
		}

class AdresseForm(forms.ModelForm):
	class Meta:
		model = Adresse
		fields = [ 'telephone', 'email', 'quartier', 'ville',]

		labels = {
			'telephone': 'Telephone',
			'email': 'Email',
			'quartier': 'Quartier ',
			'ville': 'Ville',
		}

		widgets = {
			'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le numéro',}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Saisir l\'email', }),
			'quartier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le quartier', }),
			'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la ville', }),
		}


class BanqueForm(forms.ModelForm):
	class Meta:
		model = Banque
		fields = [ 'nom', 'montant', 'validation',]

		labels = {
			'nom': 'Nom',
			'montant': 'Montant',
			'validation': 'Validation ',
		}

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'veillez saisir le nom de la banque',}),
			'montant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le montant', }),
			'validation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'La validation', }),
		}


class RecuForm(forms.ModelForm):
	class Meta:
		model = Recu
		fields = [ 'date', 'montant', 'reste', 'numero', 'employe', ]

		labels = {
			'date': 'Date',
			'montant': 'Montant',
			'reste': 'Reste ',
			'numero': 'Numero ',
			'employe': 'employe ',
		}

		widgets = {
			'date': forms.TextInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'montant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le montant', }),
			'reste': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le reste', }),
			'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le numero', }),
			'employe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'L\'employé', }),


		}


