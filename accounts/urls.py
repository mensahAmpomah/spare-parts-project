from django.urls import path
from .views import( registerUser,user_login,logoutView, edit,
                   UserListCreateAPI,UserDetailAPI,
                   UserProfileListCreateAPI,UserProfileDetailAPI)


urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('login/', user_login, name='login'),
    path('logout/', logoutView, name='logout'),
    path('edit/',edit, name='edit'),


    path("api/users/", UserListCreateAPI.as_view(), name="user-list"),
    path("api/users/<int:pk>/", UserDetailAPI.as_view(), name="user-detail"),
    path("api/profiles/", UserProfileListCreateAPI.as_view(), name="profile-list"),
    path("api/profiles/<int:pk>/", UserProfileDetailAPI.as_view(), name="profile-detail"),
] 