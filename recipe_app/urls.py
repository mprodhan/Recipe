from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from recipe_app import views

urlpatterns = [

    path('', views.index, name='homepage'),
    path('recipe_add/', views.recipe, name='recipe_add'),
    path('recipe_detail/<str:username>/', views.recipedetail, name='recipe'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)