from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import bcrypt

# Create your views here.
def index(request):
    
    return render(request, 'login/index.html')

def login(request):
    if request.method != "POST":
        return redirect('/')
    email = request.POST['email']
    user = User.objects.filter(email = email)
    
    if len(user) == 0:
        messages.error(request, "This email {} does not exist in the system".format(email), extra_tags="login")
        # messages.add_message(request,messages.WARNING)
    else:
        password = request.POST['password']
        # To check if a password encrypted in bcrypt matches another
        user = user.first()
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            messages.error(request, "Incorrect password.", extra_tags="login")
            return redirect('/')
        messages.success(request, "Successfully logged in !, Welcome {} {}".format(user.first_name, user.last_name))
        return redirect('/login/sucess')

    return redirect('/')

def create(request):
    if request.method != "POST":
        return redirect('/')
        
    # Validation for creating new object
    errors = User.objects.create_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            # messages.error(request, error, extra_tags=tag)
            messages.error(request, error, extra_tags="create")
        return redirect('/')

    password = request.POST['password']
    # Encript the password by using bscrypt
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    newuser = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
    # messages.success(request, "Sucessfully logged in!", extra_tags="sucess")
    messages.success(request, "Sucessfully logged in!")
    return redirect('/login/sucess')

def sucess(request):
    # Display sucess message
    return render(request, 'login/sucess.html')