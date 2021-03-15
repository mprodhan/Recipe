from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as recipe_logout
from django.contrib.auth.forms import UserCreationForm

from auth.forms import LoginForm, SignUpForm

def signupview(request):
    html = "signup.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, html, context)

def loginview(request):
    html = "login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, html, context)

def logout(request):
    recipe_logout(request)
    return HttpResponseRedirect(reverse('homepage'))