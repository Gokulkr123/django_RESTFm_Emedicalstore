from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


# create Product list function
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})
# read function
def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

#update function
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})


#delete function

from django.shortcuts import render
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrieveproduct')
    
    return render(request,'delete.html',{'product':product})

# search function

# views.py
from django.shortcuts import render
from .models import Product

def productsearch(request):
    data = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=data)# icotains case insensitive function
    return render(request, 'searchresults.html', {'products': products, 'data': data})

