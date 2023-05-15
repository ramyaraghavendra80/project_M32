from django.urls import path
from .views import Productlist, Productdetails

urlpatterns=[
    path('products/', Productlist.as_view()),
    path('products/<int:product_id>/', Productdetails.as_view()),

]