from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home, name='home'),
    path('post/', views.BlogFormView, name='post'),
    path('blog-details/<slug:slug>', views.BlogDetails, name='blog_details'),
    path('blog-category/<int:pk>', views.CategoryBlogs, name='blog-category'),
]