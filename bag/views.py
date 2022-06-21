from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request,
                         (f'Removed {product.name} '
                          f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        if item_id == '0':
            request.session['bag'] = {}
            request.session['order_info'] = {}
            messages.success(request, 'Your bag is now empty')
            return redirect(reverse('view_bag'))
        else:
            product = get_object_or_404(Product, pk=item_id)
            bag = request.session.get('bag', {})
            bag.pop(item_id)
            request.session['bag'] = bag
            messages.success(request, f'{product.name} removed from bag')
            return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing {product.name} from bag')
        return HttpResponse(status=500)
