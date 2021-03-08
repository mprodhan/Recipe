from django.shortcuts import render
from recipe_app.models import Food

def index(request):
    html = "index.html"
    data = Food.objects.all()
    return render(request, data, html)
