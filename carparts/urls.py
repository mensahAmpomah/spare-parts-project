from django.urls import path
from . import views

urlpatterns = [
    path('select-car/', views.select_car, name='select-car'),
    # path('spare-parts/<int:car_id>/', views.view_spare_parts, name='view_spare_parts'),
]