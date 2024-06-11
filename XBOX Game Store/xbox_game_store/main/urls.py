from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('personal-data/', views.personal_data, name='personal-data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)