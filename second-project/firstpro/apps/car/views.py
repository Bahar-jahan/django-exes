from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    car_brand = CarBrand.objects.all()
    context = {
        'welcome': 'به صفحه ماشین ها  خوش امدید',
        'carList': car_brand
    }
    return render(request, 'car/index.html', context)


def Pride(request):
    car = CarBrand.objects.get(name='پراید')
    context = {
        'welcome': 'به صفحه پراید خوش امدید',
        'car': car,
        'range': range(1, 10)
    }
    return render(request, 'car/pride.html', context)


def Lamborghini(request):
    car = CarBrand.objects.get(name='لامبورگینی')
    context = {
        'welcome': 'به صفحه Lamborghini خوش امدید',
        'range': range(1, 10),
        'car': car,
    }
    return render(request, 'car/lamborgini.html', context)


def Order(request):
    context = {
        'welcome': 'به صفحه سفارش خوش امدید'
    }
    return render(request, 'car/order.html', context)
