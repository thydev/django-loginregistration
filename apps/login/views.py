from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    
    return render(request, 'login/index.html')

def login(request):
    if request.method != "POST":
        return redirect('/')

def create(request):
    if request.method != "POST":
        return redirect('/')
        
    # Validation for creating new object
    errors = User.objects.create_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    password = request.POST['password']
    newuser = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
    # messages.success(request, "Sucessfully logged in!", extra_tags="sucess")
    messages.success(request, "Sucessfully logged in!")
    return redirect('/login/sucess')

def sucess(request):
    # Display sucess message
    return render(request, 'login/sucess.html')