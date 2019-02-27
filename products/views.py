from django.shortcuts import render, get_object_or_404
from .models import Product


def product_view(request):
    product_list = Product.objects.order_by('price')[:5]
    return render(request, 'products.html', {"products": product_list})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})