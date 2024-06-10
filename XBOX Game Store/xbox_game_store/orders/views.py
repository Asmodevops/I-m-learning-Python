from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from orders.models import Cart, CartItem
from store.models import Game


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Game, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    next_page = request.POST.get('next', None)

    if next_page is not None:
        return redirect(next_page)
    else:
        return redirect('users:profile')




@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()

    return redirect('users:profile')


@login_required
def increase(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('users:profile')


@login_required
def decrease(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('users:profile')