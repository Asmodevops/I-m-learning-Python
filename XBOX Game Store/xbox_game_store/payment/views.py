import uuid
import json

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
import os
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Configuration
from orders.models import Cart, Purchase, PurchaseItem
from payment.models import PaymentStatus
from store.models import GamePass


load_dotenv()

Configuration.account_id = os.getenv('SHOP_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')

def create_payment(price, title, meta):
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            # "return_url": "http://127.0.0.1:8000/"
            "return_url": "https://af70-185-13-176-72.ngrok-free.app/payment/payment_complete/"
        },
        "capture": True,
        "description": title,
        "metadata": meta
    }, payment_id)

    return payment


def send_telegram_message(text):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('ADMIN_TELEGRAM_USER_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()


@login_required
def gamepass_pay(request, object_id):
    object = GamePass.objects.get(id=object_id)
    meta = {
        'type': 'GAMEPASS',
        'object_id': object_id,
        "user_id": request.user.id,
    }

    try:
        payment = create_payment(object.price, f'GAMEPASS {object_id} {object.title}', meta)
    except Exception as e:
        return redirect('users:profile')

    return redirect(payment.confirmation.confirmation_url)


@login_required
def cart_pay(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    total_price = cart.get_total_price()
    total_items = cart.items.count()

    meta = {
        'type': 'GAME',
        "user_id": request.user.id,
    }

    try:
        payment = create_payment(total_price, f'GAME {total_items}', meta)
    except Exception as e:
        return redirect('users:profile')

    return redirect(payment.confirmation.confirmation_url)


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_object = payload['object']
        item_type = payment_object['metadata']['type']
        user_id = int(payment_object['metadata']['user_id'])
        user = get_object_or_404(User, id=user_id)
        status = payment_object['status']

        if status == 'succeeded':
            payment_status, created = PaymentStatus.objects.get_or_create(user=user)
            payment_status.is_payment_complete = True
            payment_status.save()

            if item_type == 'GAMEPASS':
                item_id = int(payment_object['metadata']['object_id'])
                game_pass = get_object_or_404(GamePass, id=item_id)
                purchase = Purchase.objects.create(user=user)
                content_type = ContentType.objects.get_for_model(game_pass)
                PurchaseItem.objects.create(
                    purchase=purchase,
                    content_type=content_type,
                    object_id=game_pass.id
                )

                message = f"Пользователь {user.username} ({user.email}) произвел оплату GAMEPASS {game_pass.title}"
                try:
                    send_telegram_message(message)

                except Exception as e:
                    pass

            elif item_type == 'GAME':
                cart = get_object_or_404(Cart, user=user)
                purchase = Purchase.objects.create(user=user)
                purchased_games = []
                for cart_item in cart.items.all():
                    content_type = ContentType.objects.get_for_model(cart_item.product)
                    PurchaseItem.objects.create(
                        purchase=purchase,
                        content_type=content_type,
                        object_id=cart_item.product.id,
                        quantity=cart_item.quantity
                    )
                    purchased_games.append(f"{cart_item.product.title} - {cart_item.quantity} шт.")

                cart.items.all().delete()
                purchased_games = '\n'.join(purchased_games)
                message = f"Пользователь {user.username} ({user.email}) произвел оплату игр: \n{purchased_games}"
                try:
                    send_telegram_message(message)

                except Exception as e:
                    pass

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


@login_required
def payment_complete(request):
    payment_status = get_object_or_404(PaymentStatus, user=request.user)

    if not payment_status.is_payment_complete:
        return redirect('homepage')

    payment_status.is_payment_complete = False
    payment_status.save()

    data = {
        'title': 'Платеж завершен'
    }
    return render(request, 'payment/payment_complete.html', data)