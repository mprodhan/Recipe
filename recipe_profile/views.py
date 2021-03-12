from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from recipe_app.models import Food
from recipe_user.models import RecipeUser
from blog.models import Blog

def profileview(request, id):
    html = "profile.html"
    profilers = RecipeUser.objects.get(id=id)
    profilers = request.user
    profiles = Food.objects.filter(id=id)
    blogs = Blog.objects.filter(id=id)
    context = {'profilers': profilers, 'profiles': profiles, \
        'blogs': blogs}
    return render(request, html, context)
