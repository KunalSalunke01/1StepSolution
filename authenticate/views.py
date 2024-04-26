from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

# Create your views here.

def login(request):

    # if (request.method=="POST"):
    #     print("This is post request")
    # else:
    #     print("This is get request")

    if (request.method=="POST") :   #if Post request
        #storing value in variable
        username = request.POST['email']
        userpassword = request.POST['pass1']
        #checking email and password
        myuser = authenticate(username= username,password = userpassword)

        if myuser is not None:
            auth_login(request,myuser)
            messages.success(request,"Login Successfully")
            return redirect("/")
        else :
            messages.error(request,"Invalid Credentials")
            return redirect("/auth/login")
        
    return render(request,"shop/login.html")    #if not post request


def register(request):
    if (request.method=="POST") :   #if Post request
        #storing value in variable
        email=request.POST['email']
        password = request.POST['pass1']
        conf_password = request.POST['pass2']
        name = request.POST['name']
        #checking pass1==pass2
        if (password!=conf_password) :
            messages.error(request,"Password does not match")
            return render(request,"shop/register.html")
        #checking email already exists or not
        try:
            if User.objects.get(username=email) :
                messages.warning(request,"User already exists")
                return render(request,"shop/login.html")
        except Exception as identifier:
            pass
        #storing user in database
        user = User.objects.create_user(email,email,password,first_name=name,last_name="-")  # username,email,password,first_name,last_name
        user.save()
        messages.success(request,"User Registered Successfully")   
        return render(request,"shop/login.html")  

    return render(request,"shop/register.html")     #if not Post request


def logout(request):
    auth_logout(request)
    messages.info(request,"Logout Successfully")
    return redirect("/")

