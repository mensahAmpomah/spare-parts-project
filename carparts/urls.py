from django.urls import path
from . import views

urlpatterns = [
    path('select-car/', views.select_car, name='select-car'),
    path('spare-parts/<int:car_id>/', views.view_spare_parts, name='spare_parts'),
    path("shops/", views.shop_list, name="shop_list"),
    path("shops/<int:shop_id>/", views.shop_detail, name="shop_detail"),
]