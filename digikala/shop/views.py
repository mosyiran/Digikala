from django.shortcuts import render,HttpResponse
from .models import Product



def helloworld(request):
    all_products = Product.objects.all()
    # return HttpResponse(all_products)
    return render(request,'index.html', {'products':all_products})



