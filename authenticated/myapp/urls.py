from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index_page"),
    path('login/', views.loginPage, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('profile/', views.profile, name='user_profile_page'),
]
