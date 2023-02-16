from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
   path('register/', views.RegisterView, name='register'),
   path('login/', views.UserLoginView, name='login'),
   path('logout/', views.LogoutView, name='logout'),
   path('profile/', views.UserProfileView, name='profile'),
   path('profile-form/', views.ProfileFormView, name='profile-form'),

]