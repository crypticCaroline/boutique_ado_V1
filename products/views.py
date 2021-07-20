from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """A view to return product pagem including sort and seach"""
    
    product = Product.objects.all()

    context = {
        'products': product,
    }
    return render(request, 'products/products.html', context)