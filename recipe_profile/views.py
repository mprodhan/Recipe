from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required

from recipe_app.models import Food
from recipe_user.models import RecipeUser
from blog.models import Blog

@login_required
def profileview(request, username):
    html = "profile.html"
    profilers = RecipeUser.objects.get(username=username)
    profilers = request.user
    profiles = Food.objects.filter(recipe_author=profilers)
    blogs = Blog.objects.filter(blog_author=profilers)
    context = {'profilers': profilers, 'profiles': profiles, \
        'blogs': blogs}
    return render(request, html, context)
