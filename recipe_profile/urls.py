from django.urls import path
from recipe_profile import views

urlpatterns = [
    path('profile/<str:username>/', views.profileview, name='profile'),
    path('profile_image/', views.profile_image, name='profile_image')
]