from django.urls import path, include
from .views import home, About, Services, Contact, Certificat
from uzb.views import home_uz, About_uz, Services_uz, Contact_uz, Certificat_uz
from rus.views import home_ru, About_ru, Services_ru, Contact_ru, Certificat_ru
urlpatterns = [
    path('', home, name='home'),
    # path('products/<int:id>', products, name='products'),
    path('about', About, name='about'),
    path('services', Services, name='services'),
    path('Contact', Contact, name='Contact'),
    path('Certificat', Certificat, name='Certificat'),

    # uzb
    path('uz', home_uz, name='home_uz'),
    path('about_uz', About_uz, name='about_uz'),
    path('services_uz', Services_uz, name='services_uz'),
    path('Contact_uz', Contact_uz, name='Contact_uz'),
    path('Certificat_uz', Certificat_uz, name='Certificat_uz'),
    # ru
    path('ru', home_ru, name='home_ru'),
    path('about_ru', About_ru, name='about_ru'),
    path('services_ru', Services_ru, name='services_ru'),
    path('Contact_ru', Contact_ru, name='Contact_ru'),
    path('Certificat_ru', Certificat_ru, name='Certificat_ru'),
]
