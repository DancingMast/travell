from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from favourite import favourite
from tour.models import userfavs
from tour.models import comfavs


# Create your views here.

def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['name']
        username = request.POST['userid']
        email = request.POST['e-mail']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            print("username already taken!")
            messages.info(request,'Username already Taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            print("E-mail already taken!")
            messages.info(request,'Email already Taken!')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name)
            user.save()
            print ("User Created")
            return redirect('register')
    
    else:
        return render(request,'login.html')


def login(request):
    
    if(request.method == 'GET'):
    
        username = request.GET['userid']
        password = request.GET['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials!') 
            return redirect('register')   
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def showpof(request):
    name = str(request.user.first_name)
    username = str(request.user.username)
    email = str(request.user.email)
    lastlogin = str(request.user.last_login)
    datejoined = str(request.user.date_joined)

    useTowns = []
    useDests = []

    for ob in userfavs.objects.all().filter(username=username):
        useDests.append((ob.destination))
        useTowns.append((ob.town))

    Dests = zip(useDests, useTowns)

    context = {
        'name' : name,
        'email' : email,
        'lastlogin' : lastlogin,
        'datejoined' : datejoined,
        'userid' : username,
        'Dests' : Dests
    }
    return render(request,'usepof.html', context)


def max_visit(request):

        
        disthis = []
        for ob in comfavs.objects.all().order_by('-count'):
            # comTowns.append(ob.town)
            # comDests.append(ob.destination)
            disthis.append(ob.destination)
            disthis.append(ob.town)

        context = {
            'mylist': disthis,
        }
        print(context)

        return render(request, 'proj22.html', context)

