from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from recipe_app.models import Food
from recipe_user.models import RecipeUser
from recipe_app.forms import RecipeForm
from blog.models import Blog

def index(request):
    html = "index.html"
    data = Food.objects.all()
    writes = Blog.objects.all()
    context = {'data': data, 'writes': writes}
    return render(request, html, context)

@login_required
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

@login_required
def recipedetail(request, id):
    html = "recipe_view.html"
    author = RecipeUser.objects.get(id=id)
    author = request.user
    recipe = Food.objects.filter(id=id)
    context = {'author': author, 'recipe': recipe}
    return render(request, html, context)