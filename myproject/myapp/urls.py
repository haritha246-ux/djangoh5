from django.urls import path
from . import views
urlpatterns = [
  path('',views.home, name='home'),
  path('first/',views.firstpage, name='first'),
  path('second/',views.secondpage, name='second'),
  path('hellop/',views.html_page, name='hello'),
]
