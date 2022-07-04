from django.shortcuts import render

from products.models import Product, Category

# Create your views here.

def index(request):
    """ A view to return the index page """

    featured_products_list = Product.objects.filter(featured=True)
    context = {'featured_products_list': featured_products_list}
    return render(request, 'home/index.html', context)
