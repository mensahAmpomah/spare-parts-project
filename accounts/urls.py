from django.urls import path
from .views import registerUser,login


urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('login/', login, name='login'),
] 