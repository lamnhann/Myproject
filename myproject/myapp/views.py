from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature, New_Feature

# Create your views here.
# def index(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'Fast'
#     feature1.is_true = True
#     feature1.details = 'Our service is very quick'
    
#     feature2 = Feature()
#     feature2.id = 1
#     feature2.name = 'Reliable'
#     feature2.is_true = True
#     feature2.details = 'Our service is very Reliable'
    
#     feature3 = Feature()
#     feature3.id = 2
#     feature3.name = 'Easy To Use'
#     feature3.is_true = False
#     feature3.details = 'Our service is easy to use'
    
#     feature4 = Feature()
#     feature4.id = 3
#     feature4.name = 'Affonable'
#     feature4.is_true = True
#     feature4.details = 'Our service is very Affonable'
    

#     features = [feature1, feature2, feature3, feature4]
#     return render(request, 'index.html', {'features': features})

def index(request):
    features = Feature.objects.all()
    new_feature = New_Feature.objects.all()
    return render(request, 'index.html',{'features' : features , 'new_features': new_feature})

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
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password no the same')
            return redirect('register')
    else:          
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
       
        #Check user đã register chưa
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1, 2, 3, 4, 5, 'tom', 'tim', 'john']
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})