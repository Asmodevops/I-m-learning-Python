import uuid
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import os

from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Configuration
from yookassa.domain.notification import WebhookNotification

from orders.models import Cart, Purchase, PurchaseItem
from store.models import Game, GamePass

load_dotenv()

Configuration.account_id = os.getenv('SHOP_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')

def create_payment(price, title, user_id):
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            # "return_url": "http://127.0.0.1:8000/"
            "return_url": "https://2640-185-13-176-135.ngrok-free.app/"
        },
        "capture": True,
        "description": title,
        "metadata": {
            "user_id": str(user_id)
        }
    }, payment_id)

    return payment


@login_required
def gamepass_pay(request, object_id):
    object = GamePass.objects.get(id=object_id)
    try:
        payment = create_payment(object.price, f'GAMEPASS {object_id} {object.title}', request.user.id)
    except Exception as e:
        return HttpResponse('<h1>Не удалось</h1>')

    return redirect(payment.confirmation.confirmation_url)


@login_required
def cart_pay(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    total_price = cart.get_total_price()
    total_items = cart.items.count()

    try:
        payment = create_payment(total_price, f'GAME {total_items}', request.user.id)
    except Exception as e:
        return HttpResponse('<h1>Не удалось</h1>')

    return redirect(payment.confirmation.confirmation_url)


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        payment_object = payload['object']
        description_parts = payment_object['description'].split()
        item_type = description_parts[0]
        user_id = int(payment_object['metadata']['user_id'])
        user = get_object_or_404(User, id=user_id)
        status = payment_object['status']

        if status == 'succeeded':
            if item_type == 'GAMEPASS':
                item_id = int(description_parts[1])
                game_pass = get_object_or_404(GamePass, id=item_id)
                purchase = Purchase.objects.create(user=user)
                content_type = ContentType.objects.get_for_model(game_pass)
                PurchaseItem.objects.create(
                    purchase=purchase,
                    content_type=content_type,
                    object_id=game_pass.id
                )

            elif item_type == 'GAME':
                cart = get_object_or_404(Cart, user=user)
                purchase = Purchase.objects.create(user=user)
                for cart_item in cart.items.all():
                    content_type = ContentType.objects.get_for_model(cart_item.product)
                    PurchaseItem.objects.create(
                        purchase=purchase,
                        content_type=content_type,
                        object_id=cart_item.product.id,
                        quantity=cart_item.quantity
                    )

                cart.items.all().delete()

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


