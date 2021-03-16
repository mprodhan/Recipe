from django.urls import path
from recipe_profile import views

urlpatterns = [
    path('profile/<str:username>/', views.profileview, name='profile'),
]