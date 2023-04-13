from django.urls import path
from .views import *

urlpatterns=[
    path('', Basketsummary.as_view(), name='basket_summary'),
    path('add/', Addbasket.as_view(), name='basket_add'),
    path('update/', Updatebasket.as_view(), name='basket_update'),
    path('delete/', Deletebasket.as_view(), name='basket_delete')

]


# from django.urls import path

# from . import views

# app_name = 'basket'

# urlpatterns = [
#     path('', views.basket_summary, name='basket_summary'),
#     path('add/', views.basket_add, name='basket_add'),
#     path('delete/', views.basket_delete, name='basket_delete'),
#     path('update/', views.basket_update, name='basket_update'),
# ]