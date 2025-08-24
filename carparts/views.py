from django.shortcuts import render,get_object_or_404
from .models import Car, SparePart

def select_car(request):
    cars = Car.objects.all()
    return render(request, 'carparts/selectcar.html', {'cars': cars})

# def view_spare_parts(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     spare_parts = car.SparePart.all()  # Uses related_name
#     return render(request, 'view_spare_parts.html', {'car': car, 'spare_parts': spare_parts})

