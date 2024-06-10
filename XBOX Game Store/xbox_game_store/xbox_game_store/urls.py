from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('users/', include('users.urls', namespace="users")),
    path('feedback/', include('feedback.urls', namespace="feedback")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('payment/', include('payment.urls', namespace="payment")),
]

handler404 = 'store.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

