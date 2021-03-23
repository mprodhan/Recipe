from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required

from recipe_app.models import Food
from recipe_user.models import RecipeUser
from blog.models import Blog
from recipe_profile.models import ProfileImage
from recipe_profile.forms import ImageForm

@login_required
def profileview(request, username):
    html = "profile.html"
    profilers = RecipeUser.objects.get(username=username)
    profilers = request.user
    profiles = Food.objects.filter(recipe_author=profilers)
    blogs = Blog.objects.filter(blog_author=profilers)
    images = ProfileImage.objects.filter(profile_image=profilers)
    context = {'profilers': profilers, 'profiles': profiles, \
        'blogs': blogs, 'images': images}
    return render(request, html, context)

@login_required
def profile_image(request):
    html = "profile_image.html"
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            ProfileImage.objects.create(
                profile_image=data['profile_image']
            )
            return HttpResponseRedirect(reverse('profile', args=(request.user.username,)))
    else:
        form = ImageForm()
    context = {'form': form}
    return render(request, html, context)

