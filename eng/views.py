from django.shortcuts import render
from eng.models import *


# Create your views here.
def home(request):
    sher = About_one.objects.order_by('-id')[:1]
    home1 = Home.objects.order_by('-id')[:3]
    product = Product.objects.order_by('-id')[:3]
    statistika_text = Statistika_text.objects.order_by('-id')[:1]
    statistika = Statistika.objects.order_by('-id')[:4]
    lon = Aqili_gap.objects.all()
    logo = Logo.objects.all()
    # about_one = About.objects.all()
    if request.method == "POST":
        contact = Contact(request)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        # contact.save()
    ctx = {
        'home1': home1,
        'product': product,
        'statistika_text': statistika_text,
        'statistika': statistika,
        'sher': sher,
        'lon': lon,
        'logo': logo
        # 'about_one':about_one
    }
    return render(request, 'en/index.html', ctx)


def About(request):
    sher = About_one.objects.order_by('-id')[:1]
    statistika_text = Statistika_text.objects.order_by('-id')[:1]
    statistika = Statistika.objects.order_by('-id')[:4]
    team = Factory_about.objects.order_by('-id')[:4]
    lon = Aqili_gap.objects.all()
    ctx = {
        'lon': lon,
        'statistika': statistika,
        'statistika_text': statistika_text,
        'sher': sher,
        'team': team
    }
    return render(request, 'en/about.html', ctx)


def Services(request):
    category = Category_product.objects.all()
    product = Product.objects.all()
    logo = Logo.objects.all()
    ctx = {
        'category': category,
        'product': product,
        'logo': logo
    }
    return render(request, 'en/services.html', ctx)


def Contact(request):
    logo = Logo.objects.all()
    ctx = {
        'logo': logo
    }
    return render(request, 'en/contact.html', ctx)


def Certificat(request):
    category = Category_certificat.objects.all()
    product = Certificats.objects.all()
    logo = Logo.objects.all()
    ctx = {
        'category': category,
        'product': product,
        'logo': logo
    }
    return render(request, 'en/sertificat.html', ctx)
