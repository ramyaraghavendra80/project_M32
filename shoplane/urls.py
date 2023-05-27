from django.urls import path
from .views import Productlist, Productdetails, ProductReview, SearchView, MyCartView, CartView, UpdateCart, CheckoutView, UserSignup, UserSignin
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('products/', Productlist.as_view(),name="product"),
    path('products/<int:product_id>/', Productdetails.as_view(), name="product_id"),
    path('products/<int:product_id>/reviews/', csrf_exempt(ProductReview.as_view()), name="product_review"),
    path('products/search/', csrf_exempt(SearchView.as_view()), name="product_search"),
    path('products/<int:cart_id>/mycartview/', csrf_exempt(MyCartView.as_view()), name="my_cart_view"),
    path('products/<int:cart_id>/cartview/', csrf_exempt(CartView.as_view()), name="cart_view"),
    path('cartview/updatecart/<int:cart_id>/', csrf_exempt(UpdateCart.as_view()), name="update_cart"),
    path('cartview/updatecart/<int:cart_id>/checkoutcart/', csrf_exempt(CheckoutView.as_view()), name="checkout_cart"),
    path('user/signup/', csrf_exempt(UserSignup.as_view()), name="user_signup"),
    path('user/signin/', csrf_exempt(UserSignin.as_view()), name="user_signin"),

]