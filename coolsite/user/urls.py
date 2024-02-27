from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
    path('registration/', views.registration),
]