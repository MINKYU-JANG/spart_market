from django.shortcuts import get_object_or_404, redirect, render
from products.forms import ProductForm
from products.models import Product
from django.views.decorators.http import require_POST


def list_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/list.html', context)


def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    context = {'form': form}
    return render(request, 'products/create.html', context)


def detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/detail.html', context)


def update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('products:list')
    context = {'form': form}
    return render(request, 'products/create.html', context)


@require_POST
def delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products:list')
