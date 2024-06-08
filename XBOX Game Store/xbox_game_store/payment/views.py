import uuid

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import os

from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Configuration
from yookassa.domain.notification import WebhookNotification

from orders.models import Cart
from store.models import Game, GamePass

load_dotenv()

Configuration.account_id = os.getenv('SHOP_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')

def create_payment(price, title):
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000/"
        },
        "capture": True,
        "description": title,
    }, payment_id)

    return payment


@login_required
def gamepass_pay(request, object_id):
    object = GamePass.objects.get(id=object_id)
    try:
        payment = create_payment(object.price, f'Game Pass {object.title}')
    except Exception as e:
        return HttpResponse('<h1>Не удалось</h1>')

    return redirect(payment.confirmation.confirmation_url)


@login_required
def cart_pay(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    total_price = cart.get_total_price()
    total_items = cart.items.count()

    try:
        payment = create_payment(total_price, f'{total_items} games')
    except Exception as e:
        return HttpResponse('<h1>Не удалось</h1>')

    return redirect(payment.confirmation.confirmation_url)




# @csrf_exempt
# def yookassa_webhook(request):
#     if request.method == 'POST':
#         # Получаем JSON из тела запроса
#         try:
#             notification = WebhookNotification(request.body)
#         except Exception as e:
#             return JsonResponse({'message': str(e)}, status=400)
#
#         # Далее можно обработать уведомление
#         # Например, проверить статус платежа и выполнить действия в зависимости от этого статуса
#
#         # Пример обработки уведомления
#         payment_id = notification.object.id
#         event_type = notification.event.type
#         status = notification.object.status
#
#         # Дополнительная обработка статуса платежа
#         # Например, обновление статуса платежа в вашей базе данных
#
#         return JsonResponse({'message': 'Уведомление успешно обработано'}, status=200)
#     else:
#         return JsonResponse({'error': 'Метод не поддерживается'}, status=405)