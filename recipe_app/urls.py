from django.urls import path
from recipe_app import views

urlpatterns = [

    path('', views.index, name='homepage'),

]