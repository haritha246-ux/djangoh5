from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ps/',views.product_list,name='productlist'),
    path('cv/',views.carousel_view,name='carousel_view'),
    path('gv/',views.grids_view,name='grids_view'),
]