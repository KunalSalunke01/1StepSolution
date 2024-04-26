from django.shortcuts import render,HttpResponse,redirect
from shop.models import Contact,Product
from django.contrib import messages
from math import ceil
import os
from datetime import date
# Create your views here.

def index(request):

    allProds =[]
    cateprods = Product.objects.values('category','id')
    cates = {item['category'] for item in cateprods}
    for cate in cates:
        prod = Product.objects.filter(category=cate)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}

    return render(request,"shop/index.html",params)


def productView(request,prodId):   #search
    if request.user.is_authenticated:
        if Product.objects.filter(id=prodId) :
                myproduct= Product.objects.filter(id=prodId)
                context={"myproduct":myproduct}
                return render(request,"shop/productView.html",context)
        else:
            messages.warning(request,"No such Product")
            return render(request,"shop/index.html")
    else:
        messages.warning(request,"Please Login first..")
        return redirect("../auth/login")
    #storing search key
    searchprod= request.POST.get("searchcate")
    allProds =[]
    #filter products
    prod = Product.objects.filter(category=searchcate)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))     #find no of slides req
    allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}

    return render(request,"shop/products.html",params)


def contact(request):
    if (request.method=="POST") :   #if Post request
        #storing value in variable
        name = request.POST.get('name')
        mobno= request.POST.get('mobno')
        email= request.POST.get('email')
        curr_year= request.POST.get('curr_year')
        desc= request.POST.get('desc')
        myquery= Contact(name=name,mobno=mobno,email=email,curr_year=curr_year,desc=desc)
        myquery.save()
        messages.warning(request,"Request Submitted Successfully\nWe will get back to You..")
        return redirect("/")
    return render(request,"shop/contact.html")

def sell(request):
    if (request.method=="POST") :   #if Post request
        #storing value in variable
        product_name = request.POST.get('prodname')
        desc= request.POST.get('desc')
        category=request.POST.get('category')
        subcate = request.POST.get('subcategory')
        subcategory= subcate.lower()

        if len(request.FILES)!=0 :
            image = request.FILES['picfile']
        price=request.POST.get('price')
        condn=request.POST.get('condition')
        curr_year= request.POST.get('year')
        contact= request.POST.get('contact')
        email= request.POST.get('email')
        pub_date = date.today()
        seller_name=request.POST.get('sellername')
        mypost= Product(product_name=product_name,mobno=contact,seller_name=seller_name,pub_date=pub_date,email=email,curr_year=curr_year,desc=desc,category=category.lower(),subcategory=subcategory.lower(),image=image,price=price,condn=condn)
        mypost.save()
        messages.success(request,"Post Submitted Successfully\nYour Ad will go live soon..")
        return redirect("/")
    
    if request.user.is_authenticated :      #if not post
        return render(request,"shop/listprod.html") 
    else:
        messages.warning(request,"Please Login first..")
        return render(request,"shop/login.html")    


def search(request):
    if request.method=="POST" :
        #storing search key
        searchcate= request.POST.get("searchcate")
        allProds =[]
        #filter products
        prod = Product.objects.filter(subcategory=searchcate.lower())
        n = len(prod)
        if n != 0 :
            nSlides = n // 4 + ceil((n / 4) - (n // 4))     #find no of slides req
            allProds.append([prod,range(1,nSlides),nSlides])
            params={'allProds':allProds}
            return render(request,"shop/products.html",params)
        else:
            messages.warning(request,"Sorry! No Product Found..")
            return redirect("/")
    else:
        return redirect("/")

def category(request,catname):
        prod=Product.objects.filter(category=catname)
        allProds=[]
        n= len(prod)
        if n != 0 :
            nSlides = n // 4 + ceil((n / 4) - (n // 4))     #find no of slides req
            allProds.append([prod,range(1,nSlides),nSlides])
            params={'allProds':allProds}
            return render(request,"shop/products.html",params)
        else:
            messages.warning(request,"Sorry! No Product Found..")
            return redirect("/")

def about(request):
    return render(request,"shop/about.html")

#     if request.user.is_authenticated:
#         # urerfname= request.user.first_name
#         # useremail= request.user.username
#         # userlname= request.user.last_name

 
def profile(request):
    if request.user.is_authenticated:
        if Product.objects.filter(email=request.user.email) :
            allProds=[]
            prod = Product.objects.filter(email=request.user.email)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))     #find no of slides req
            allProds.append([prod,range(1,nSlides),nSlides])
            params={'allProds':allProds}
            return render(request,"shop/profile.html",params)
        else:
            return render(request,"shop/profile.html")
    else:
         messages.warning(request,"Please Login first..")
         return render(request,"shop/login.html") 
  

def editproduct(request,prodId):
    myproduct= Product.objects.get(id=prodId)
    if request.method == "POST":
        if len(request.FILES) != 0:
                if len(myproduct.image)>0 :
                    os.remove(myproduct.image.path)
                myproduct.image = request.FILES["picfile"]

        myproduct.product_name = request.POST.get('prodname')
        myproduct.desc= request.POST.get('desc')
        myproduct.category=request.POST.get('category')
        subcate = request.POST.get('subcategory')
        myproduct.subcategory= subcate.lower()
        myproduct.price=request.POST.get('price')
        myproduct.condn=request.POST.get('condition')
        myproduct.seller_name=request.POST.get('sellername')
        myproduct.curr_year= request.POST.get('year')
        myproduct.mobno= request.POST.get('contact')
        myproduct.email= request.POST.get('email')   
        myproduct.pub_date = date.today() 
        myproduct.save()
        messages.success(request,"Product Updated Successfully..")
        return redirect("/")
    
    context={"myproduct":myproduct}
    return render(request,"shop/editprod.html",context)
  

def deleteproduct(request,prodId):
    myproduct = Product.objects.get(id=prodId)
    if len(myproduct.image)>0 :
        os.remove(myproduct.image.path)
    myproduct.delete()
    messages.error(request,"Product Deleted Successfully..")
    return redirect("/")
