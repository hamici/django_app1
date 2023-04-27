from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .form import productAddForm
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
def productAdd(request):
    if request.method == 'POST':
        productForm = productAddForm(request.POST)
        productForm.save()
        return redirect('/product/list')
    else:
        productForm = productAddForm()
    return render(request,'productAdd.html',{'form':productForm})
def productDetail(request,id):
    product = Product.objects.get(id=id)
    context= {
        'id' : id,
        'product' : product
    }
    return render(request,'productDetail.html',context)
def productDelete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/product/list')
def productEdit(request,id):
    product= Product.objects.get(id=id)
    if request.method == 'POST':
        productForm = productAddForm(request.POST,instance=product)
        productForm.save()
        return redirect('/product/list')
    else:
        productForm = productAddForm(instance=product)
    return render(request,'productEdit.html',{'form':productForm})