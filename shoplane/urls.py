from django.urls import path
from .views import Productlist

urlpatterns=[
    path('products/', Productlist.as_view()),
]