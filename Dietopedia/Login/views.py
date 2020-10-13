from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def SignUp(request):
    if  request.method== 'POST':
        First_Name= request.POST["fname"]
        Last_Name=request.POST["lname"]
        Email= request.POST["email"]
        Password=request.POST["password"]
        CPassword=request.POST["cpassword"]
        if Password==CPassword:
            user=User.objects.create_user(username=First_Name,first_name=First_Name,last_name=Last_Name,password=Password,email=Email)
            user.save()
            print("User Created")
            return(redirect('/log/signin/'))
        else:
            messages.info(request,"Password not matching")
            return(redirect('/log/signup/'))
    else:
       return render(request,"signup.html",{})


def SignIn(request):
        if request.method == "POST":
            username=request.POST['Username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return (redirect('/profile/',{user}))
            else:
                messages.info(request,"Invalid Credentials")
                return (redirect('/log/signin'))
        else:
         return render(request,"signin.html",{})    