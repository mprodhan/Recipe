from django.urls import path
from recipe_app import views

urlpatterns = [

    path('', views.index, name='homepage'),
    path('recipe_add/', views.recipe, name='recipe_add'),
    path('recipe_detail/<str:username>/', views.recipedetail, name='recipe'),

]