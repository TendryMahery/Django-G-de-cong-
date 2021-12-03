from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.accueil, name="accueil"),
    path(r'connection',views.connection, name="connection"),
    path(r'contact',views.contact, name="contact"),
    path(r'demande',views.demande, name="demande"),
    path(r'register',views.register, name="register"),
    path(r'accueil',views.accueil, name='accueil'),
    path(r'apropos',views.apropos, name='apropos'),
    path('logout',views.deconnection, name='logout'),
    path(r'recherche',views.recherche, name='recherche'),
    path(r'delete/<str:id>',views.delete, name='delete'),
]