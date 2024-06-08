from orders.models import Cart


def cart_processor(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = None
    else:
        cart = None
    return {'cart': cart}