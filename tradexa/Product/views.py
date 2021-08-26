
from django.shortcuts import render
from.forms import ProductForm
from .models import Product

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm=ProductForm(request.POST)
        if fm.is_valid():
            
            nm = fm.cleaned_data['name']
            wt = fm.cleaned_data['weight']
            pr = fm.cleaned_data['price']
            cr = fm.cleaned_data['created_at']
            ur = fm.cleaned_data['updated_at']
            #  print(nm)
            #  print(wt)
            #  print(pr)
            #  print(cr)
            #  print(ur)
            regist = Product(name=nm, weight=wt, price=pr, created_at=cr, updated_at=ur)
            regist.save()
            
    else:
        fm=ProductForm() 
    return render(request,'Product/products.html',{'form':fm})




