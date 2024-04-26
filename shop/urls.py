from django.urls import path
from . import views,wishlistview

urlpatterns = [
    path("",views.index,name = "ShopHome"),
    path("productView/<int:prodId>",views.productView,name = "productView"),
    path("sell/",views.sell,name="Sell"),
    path("contact/",views.contact,name="ContactUs"),
    path("about/",views.about,name="AboutUs"),
    path("search/",views.search,name="Search"),
    path("profile/",views.profile,name="Profile"),
    path("editproduct/<int:prodId>",views.editproduct,name="EditProduct"),
    path("deleteproduct/<int:prodId>",views.deleteproduct,name="DeleteProduct"),
    path("category/<str:catname>",views.category,name="Category"),
    path("wishlist/",wishlistview.index,name="Wishlist"),
    path("addtowishlist/<int:prod_id>",wishlistview.addtowishlist,name="AddToWishlist"),
    path("removefromwishlist/<int:prod_id>",wishlistview.removefromwishlist,name="RemoveFromWishlist"),
    
]
