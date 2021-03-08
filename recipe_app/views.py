from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from django.shortcuts import render
from recipe_app.models import Food
from recipe_app.forms import RecipeForm

def index(request):
    html = "index.html"
    data = Food.objects.all()
    context = {'data': data}
    return render(request, html, context)

def recipe(request):
    html = "recipe.html"
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Food.objects.create(
                title=data['title'],
                ingredients=data['ingredients'],
                directions=data['directions'],
                recipe_author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, html, context)
