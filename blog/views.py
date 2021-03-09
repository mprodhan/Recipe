from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from blog.models import Blog
from blog.forms import BlogForm
from recipe_user.models import RecipeUser

def bloginsert(request):
    html = "blog.html"
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Blog.objects.create(
                title=data['title'],
                body=data['body'],
                blog_author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, html, context)

def blogdetail(request, id):
    html = "blog_view.html"
    author = RecipeUser.objects.get(id=id)
    author = request.user
    blogs = Blog.objects.filter(id=id)
    context = {'author': author, 'blogs': blogs}
    return render(request, html, context)

