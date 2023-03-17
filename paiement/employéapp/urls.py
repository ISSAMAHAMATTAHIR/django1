from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    
    path('employes_list', views.employes_list, name='employes_list'),
    path('add_employe', views.add_employe, name='add_employe'),
    path('show_employe/<employe_id>', views.show_employe, name='show_employe'),
    path('delete_employe/<employe_id>', views.delete_employe, name='delete_employe'),
    path('update_employe/<employe_id>', views.update_employe, name='update_employe'),
    

    path('adresses_list', views.adresse_list, name='adresses_list'),
    path('add_adresse', views.add_adresse, name='add_adresse'),
    path('update_adresse/<adresse_id>', views.update_adresse, name='update_adresse'),
    path('delete_adresse/<adresse_id>', views.delete_adresse, name='delete_adresse'),


    path('banque_list', views.banque_list, name='banque_list'),
    path('add_banque', views.add_banque, name='add_banque'),
    path('update_banque/<banque_id>', views.update_banque, name='update_banque'),
    path('delete_banque/<banque_id>', views.delete_banque, name='delete_banque'),


    path('recu_list', views.reu_list, name='recu_list'),
    path('add_recu', views.add_recu, name='add_recu'),
    path('update_recu/<recu_id>', views.update_recu, name='update_recu'),
    path('delete_recu/<recu_id>', views.delete_recu, name='delete_recu'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)