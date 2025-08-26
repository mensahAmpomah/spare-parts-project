from django.urls import path
from .views import registerUser,user_login,logoutView, edit


urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('login/', user_login, name='login'),
    path('logout/', logoutView, name='logout'),
    path('edit/',edit, name='edit'),
] 