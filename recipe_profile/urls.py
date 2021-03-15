from django.urls import path
from recipe_profile import views

urlpatterns = [
    path('profile/<int:id>/', views.profileview, name='profile')
]