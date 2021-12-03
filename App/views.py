from django.shortcuts import render,redirect,HttpResponse
from App.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 


# Create your views here.

def apropos (request):
    return render(request,'apropos.html')

def accueil (request):
    return render (request,'accueil.html') 

def recherche (request):
    actu = Actualite.objects.all()
    ministre = Ministre.objects.all() 
    pers = Personnel.objects.all() 
    if request.GET.get('name'):
        nom = request.GET.get('name')
        pers = Personnel.objects.filter(prenom = nom)
    return render(request,'recherche.html',{'actu':actu,'ministre':ministre,'pers':pers})

@login_required(login_url='demande')
def demande (request):
    auto = Autorisation.objects.all()
    autor = Autorisation.objects.all()
    pre = Presence.objects.all()
    if request.POST.get('nom'):
        nom=  request.POST['nom']
        departement=  request.POST['departement']
        typeconge=  request.POST['typeconge']
        datedebut=  request.POST['datedebut']
        datefin=  request.POST['datefin']
        dure=  request.POST['jour']
        ma=  request.POST['ma']
        cadre=  request.POST['cadre']
        autor= Autorisation.objects.create(
            nom = nom,
            ma =ma,
            cadre = cadre,
            departement=departement,
            typeconge=typeconge,
            dure=dure,
            datedebut=datedebut,
            datefin=datefin
            
        )
        autor.save()
        messages.info(request,'Votre demande sera reçue par le DRH')
    if request.POST.get('presence'):
        pre = Presence ()
        pre.nom = request.POST.get('nomp')
        pre.status = request.POST.get('presence')
        pre.save()
        messages.info(request,'Votre présence est soingné')
    return render(request,'demande.html',{'auto':auto,'pre':pre})

def contact (request):
    if request.method == 'POST':
        nomcontact = request.POST['nomcontact']
        prenomcontact = request.POST['prenomcontact']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create(nom=nomcontact,prenom=prenomcontact,email=email,message=message)
        contact.save()
        messagecontact = messages.info(request,"Votre remarque sera reçu par l'Administrateur! mercii")
    return render(request,'contact.html')

def register (request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        immatricule = request.POST['immatricule']
        email = request.POST['email']
        password1 = request.POST['mdp1']
        password2 = request.POST['mdp2']
        if password1==password2:
            if User.objects.filter(username=immatricule).exists():
                messages.info(request,'Cette Matricule est déja utilisé')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=nom,last_name=prenom,username=immatricule,email=email,password=password1)
                user.save()
                messages.info(request,"Félicitation,vous êtes inscrit!")
                return redirect('connection') 
        else:
            messages.info(request,"Vérifié votre mot de passe")
            return redirect('register')      
    else:
        return render(request,'inscription.html')

def connection (request):
    if request.method == 'POST':
        immc = request.POST['immatriculeconne']
        password=request.POST['mdpconne']
        user = auth.authenticate(username=immc,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('demande')
        else:
            messages.info(request,"Il ya une erreur")
            return redirect('connection')
    else:
        return render(request,'connection.html')

def deconnection(request):
    auth.logout(request)
    return redirect('accueil') 

def delete(request,id):
    aut = Autorisation.objects.get(id=id)
    if request.method == "POST":
        aut.delete()
        return redirect('demande')
    return render(request,'delete.html',{'aut':aut})
