from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def view_products(request):
    products = Product.objects.all()

    context = {"products" : products}

    return render(request, "product-list.html", context)


def product_page(request, id):
    product = get_object_or_404(Product, id=id)

    context = {'product': product}

    return render(request, "product-page.html", context)