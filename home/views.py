from django.shortcuts import render

from products.models import Product, Category

# Create your views here.

def index(request):
    """ A view to return the index page """

    featured_products_list = Product.objects.filter(featured=True)
    context = {'featured_products_list': featured_products_list}
    return render(request, 'home/index.html', context)


def privacy(request):
    """
    view to display Privacy Policy
    """
    return render(request, 'home/privacy.html')


def terms(request):
    """
    view to display Terms and Conditions
    """
    return render(request, 'home/terms.html')


def contact(request):
    """
    view to display Contact Us page
    """
    return render(request, 'home/contact.html')
