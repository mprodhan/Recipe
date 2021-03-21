from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required

from blog.models import Blog
from blog.forms import BlogForm
from recipe_user.models import RecipeUser

@login_required
def bloginsert(request):
    html = "blog.html"
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Blog.objects.create(
                blog_title=data['title'],
                blog_body=data['body'],
                blog_author=data['author'],
                blog_image=data['image']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, html, context)

@login_required
def blogdetail(request, username):
    html = "blog_view.html"
    author = RecipeUser.objects.get(username=username)
    author = request.user
    blogs = Blog.objects.filter(blog_author=author)
    context = {'author': author, 'blogs': blogs}
    return render(request, html, context)

