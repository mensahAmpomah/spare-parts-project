from django.urls import path
from .views import registerUser,user_login, edit


urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('login/', user_login, name='login'),
    path('edit/',edit, name='edit'),
] 