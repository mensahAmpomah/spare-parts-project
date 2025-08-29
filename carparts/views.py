from django.shortcuts import render,get_object_or_404
from .models import Car, Shop

def select_car(request):
    cars = Car.objects.all()
    return render(request, 'carparts/selectcar.html', {'cars': cars})

def view_spare_parts(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    spare_parts = car.spare_parts.all()  
    return render(request, 'carparts/view_spare_parts.html', {'car': car, 'spare_parts': spare_parts})


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, "carparts/shop_list.html", {"shops": shops})

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    spare_parts = shop.shop_spare_parts.all()
    return render(request, "carparts/shop_detail.html", {"shop": shop, "spare_parts": spare_parts})

