from django.shortcuts import render, redirect
from flask import Flask, render_template
from django.http import HttpResponse
#from django.utils.datastructures import MultiValueDictKeyError
# from tempclass import recommend
from tp import recommend
from favourite import favourite
#from mreg import *
from .models import plotsector
from .models import userfavs
from .models import comfavs

# Create your views here.

r1=recommend()
disthis=[]
valmon : str
valcat : str
dist : str
dashvar : str
predmon : int
predyear : int
preddist : str

def realhome(request):
    return render(request,'realhome.html')

def home(request):
    return render(request,'proj.html')

def cat(request):
   global valcat 
   valcat=str(request.GET.get('cat'))
   r1.setcat(valcat)
   return render(request,"proj1.html")
    #return HttpResponse("Hello There Bazinga.."+valcat)

def catmon(request):
    global valmon,disthis,valcat
    valmon=str(request.GET.get('cat'))
    disthis=r1.setmonth(valmon)
    print (disthis)

    #mylist = zip(list1, list2)
    context = {
            'mylist': disthis,
        }
    print(context)

    return render(request, 'proj22.html', context)


    #return render_template("proj.html", len = len(disthis), disthis = disthis)
   # return render(request, 'proj2.html', context)

    #r1.clearlist()
    #return render(request,"proj2.html")

    #return HttpResponse("Hello There Bazinga..Category:  "+valcat+"  Month:  "+valmon+"\n"+str(disthis))


def dash(request):
    return render(request,"proj3.html")
    

def sect(request):
    
    plots = plotsector.objects.all()
    return render(request,"proj4.html",{"plots":plots})

def predict(request):
    
    #regretthis = r1.getgraph('PUNE')
    return render(request,"proj6.html")
    #return render(request,"proj5.html",regretthis)


def regret(request):

   global preddist,predmon,predyear
   predmon = str(request.GET.get('mon'))
   predyear = str(request.GET.get('year'))
   preddist = str(request.GET.get('dist'))
   
   regretthis = r1.getgraph(preddist,predmon,predyear)
   return render(request,"proj5.html",regretthis)

   #r1.setcat(valcat)
   
    #return render(request,"proj6.html")

def setdata(request):

    useDest = str(request.GET.get('myDest'))
    useTown = str(request.GET.get('myTown'))
    username = str(request.user.username)

    if userfavs.objects.filter(username=username).exists():
        if userfavs.objects.filter(destination=useDest).exists():
                print("Already Added to favourites!")
        
        else:
            userfav = userfavs(username = username, destination=useDest,town=useTown)
            userfav.save()
            print ("UserFav Created")
            add_data(useDest,useTown)
            #return redirect('register')
    else:
            userfav = userfavs(username = username, destination=useDest,town=useTown)
            userfav.save()
            add_data(useDest,useTown)
            print ("UserFav Created")      

    return HttpResponse('')

def add_data(useDest,useTown):

    if comfavs.objects.filter(destination=useDest).exists():
            com = comfavs.objects.get(destination=useDest)
            coun = (com.count)+1
            com.count=coun
            com.save()    
            print("Incremented in common favourites!")
    else:
            comfav = comfavs(destination=useDest,town = useTown, count = 1)
            comfav.save()
            print("Addes to Common favourites!")

    

    