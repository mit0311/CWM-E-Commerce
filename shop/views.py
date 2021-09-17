from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

# def index(request):
#     return HttpResponse("index shop")

def index(request):
    products = Product.objects.all()
    print(products)
    n=len(products)
    nslides = n//4 + ceil((n/40) - (n//4))
    params = {'no_of_slides' : nslides , 'range' : range(1,nslides),'product':products}
    return  render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productView(request):
    return HttpResponse("we are at productView")

def checkout(request):
    return HttpResponse("we are at checkout")
