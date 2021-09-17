from django.contrib import admin
from django.urls import  path
from . import  views

urlpatterns = [
    path('admin', admin.site.urls),
    path("",views.index,name='homeshop'),
    path('about/',views.about,name='about us'),
    path('contact/',views.contact,name='contact us'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('productView/',views.productView,name='productView'),
    path('checkout/',views.checkout,name='checkout'),
]