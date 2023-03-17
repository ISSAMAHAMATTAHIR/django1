from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employe, Adresse , Banque, Recu
from .forms import EmployeForm, AdresseForm, BanqueForm, RecuForm, ModelForm
from django.http import  HttpResponseRedirect

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def employes_list(request):
	employes = Employe.objects.all().order_by('nom')
	return render(request, 'employe/employes_list.html', {'employes': employes,})

def add_employe(request):
      submitted = False
      if request.method == "POST":
            form = EmployeForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_employe?submitted=True')
      else:
            form = EmployeForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'employe/add_employe.html', {
        'form': form,
        'submitted': submitted,
        })

def show_employe(request, employe_id):
    employe = Employe.objects.get(pk=employe_id)
    return render(request, 'employe/show_employe.html', {'employe': employe,})
      
def delete_employe(request, employe_id):
    employe = Employe.objects.get(pk=employe_id)
    employe.delete()
    return redirect('employes_list')


def update_employe(request, employe_id):
    employe = Employe.objects.get(pk=employe_id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('employes_list')
    return render(request, 'employe/update_employe.html', {
        'employe': employe,
        'form': form,
    })  
#Adresse liste
def adresse_list(request):
	adresses = Adresse.objects.all().order_by('email')
	return render(request, 'adresses/adresses_list.html', {'adresses': adresses,})


def add_adresse(request):
    submitted = False
    if request.method == "POST":
        form = AdresseForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_adresse?submitted=True')
    else:
        form = AdresseForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'adresses/add_adresse.html', {
        'form': form,
        'submitted': submitted,
    })

def update_adresse(request, adresse_id):
    adresse = Adresse.objects.get(pk=adresse_id)
    form = AdresseForm(request.POST or None, instance=adresse)
    if form.is_valid():
        form.save()
        return redirect('adresses_list')
    return render(request, 'adresses/update_adresse.html', {
        'adresse': adresse,
        'form': form,
    })
def delete_adresse(request, adresse_id):
    adresse = Adresse.objects.get(pk=adresse_id)
    adresse.delete()
    return redirect('adresses_list')



##pour la gestion de la banque

def banque_list(request):
	banques = Banque.objects.all().order_by('nom')
	return render(request, 'banque/banque_list.html', {'banques': banques,})


def add_banque(request):
    submitted = False
    if request.method == "POST":
        form = BanqueForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_banque?submitted=True')
    else:
        form = BanqueForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'banque/add_banque.html', {
        'form': form,
        'submitted': submitted,
    })

def update_banque(request, banque_id):
    banque = Banque.objects.get(pk=banque_id)
    form = BanqueForm(request.POST or None, instance=banque)
    if form.is_valid():
        form.save()
        return redirect('banque_list')
    return render(request, 'banque/update_banque.html', {
        'banque': banque,
        'form': form,
    })
def delete_banque(request, banque_id):
    banque = Banque.objects.get(pk=banque_id)
    banque.delete()
    return redirect('banque_list')

### Gestion de reçu

def reu_list(request):
	recus = Recu.objects.all().order_by('montant')
	return render(request, 'recu/recu_list.html', {'recus': recus,})


def add_recu(request):
    submitted = False
    if request.method == "POST":
        form = RecuForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_recu?submitted=True')
    else:
        form = RecuForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'recu/add_recu.html', {
        'form': form,
        'submitted': submitted,
    })

def update_recu(request, recu_id):
    recu = Recu.objects.get(pk=recu_id)
    form = RecuForm(request.POST or None, instance=recu)
    if form.is_valid():
        form.save()
        return redirect('recu_list')
    return render(request, 'recu/update_recu.html', {
        'recu': recu,
        'form': form,
    })
def delete_recu(request, recu_id):
    recu = Recu.objects.get(pk=recu_id)
    recu.delete()
    return redirect('recu_list')

# recherche des etudiants

def search_employe(request):
     if request.method == "GET":
          request.GET.get('query')
          if query:
               multiple_q = Q(Q(nom=query) | Q(matricule=query) | Q(id=query))
               employes = Employe.objets.filter(multiple_q)
               if employes:
                    return render(request ,'employes/employes_list.html',{'employes':employes})
               else:
                    print('Not found ...')
                    return render (request,'employes/not_fount.html',{})

