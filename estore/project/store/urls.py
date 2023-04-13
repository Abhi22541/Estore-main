from django.urls import path
from .views import *


urlpatterns=[
    path('', Allproducts.as_view(),name='Allproducts'),
    path('item/<slug:slug>/', Productdetail.as_view(), name='Productdetail'),
    path('search/<slug:cslug>/', Categorylist.as_view(), name='Categorylist'),
]