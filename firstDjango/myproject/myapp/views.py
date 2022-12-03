from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    features = Feature.objects.all()
    
    return render(request, 'firstwebpage.html', {'features': features})

def resume(request):
    features = Feature.objects.all()
    
    return render(request, 'fwb_resume.html', {'features': features})

def contact(request):
    features = Feature.objects.all()
    
    return render(request, 'contact.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(requset, 'Password Not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credantials Invalid')
            return redirect('login')
    else:    
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    entered = [1,2,3,4,5,'tim','tom','john']
    return render(request, 'counter.html', {'entered' : entered}) 

def post(request, pk):
    return render(request, 'post.html',{'pk': pk})

