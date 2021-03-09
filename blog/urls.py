from django.urls import path
from blog import views

urlpatterns = [
    path('blog_insert/', views.bloginsert, name='bloginsert'),
    path('blog_detail/<int:id>/', views.blogdetail, name='blog'),
]