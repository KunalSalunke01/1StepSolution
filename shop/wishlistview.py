from django.shortcuts import render,redirect
from shop.models import Wishlist,Product
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

#@login_required(login_url="Login")
# index displays items in wishlist
def index(request):
    if request.user.is_authenticated :
        product= Wishlist.objects.filter(user=request.user)
        context={"product":product}
        return render(request,"shop/wishlist.html",context)

    else:
        messages.warning(request,"Please Login first..")
        return redirect("/auth/login")
    
def addtowishlist(request,prod_id):
    if request.user.is_authenticated :
            # if request.method=="POST":
            # prod_id = request.POST.get("product_id")
            prod=Product.objects.get(id=prod_id)
            print(prod_id)
            print(prod)
            #check product is present in database or not
            if prod :
                if Wishlist.objects.filter(user=request.user,product=prod) :
                    messages.warning(request,'Product Already in Wishlist')
                    return redirect("/wishlist/")
                else:
                    Wishlist.objects.create(user=request.user,product=prod)
                    messages.success(request,'Product Added in Wishlist')
                    return redirect('/wishlist/')
            else:
                messages.error(request,'No such Product Found')
                return redirect("/")
    else:
        messages.warning(request,'Please Login first..')
        return redirect("/auth/login")
    
def removefromwishlist(request,prod_id):
    if request.user.is_authenticated :
        if Wishlist.objects.filter(user=request.user,product=prod_id) :
                delitem=Wishlist.objects.get(user=request.user,product=prod_id)
                delitem.delete()
                messages.warning(request,'Product Removed fron Wishlist')
                return redirect("/wishlist/")
        else:
            messages.warning(request,"No Such Product in Wishlist")
            return redirect("/wishlist/")
    else:
        messages.warning(request,'Please Login first..')
        return redirect("/auth/login")
    