from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.
def homePage(request):
    return render(request,'home.html')

def productlist(request):
    products = Product.objects.all()
    print(products)
    return render(request,'productlist.html',{'productData':products})

def productAddSimple(request):
    print('la methode utilisée :',request.method)
    print('la information post sont :', request.POST)
    if request.method == 'POST':
        print('POST')
        if 'butupd' not in request.POST:
            print('ajout')
            product= Product(name=request.POST['name'],category=request.POST['category'],price=request.POST['price'],stock_qte=request.POST['stock_qte'])
            product.save()
            return redirect('/product/list')
        else:
            print('update')

    else:
        print('other GET')
    return render(request,'productAddSimple.html')