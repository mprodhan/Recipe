from django import forms
from blog.models import Blog
from recipe_user.models import RecipeUser

class BlogForm(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=RecipeUser.objects.all())
    image = forms.FileField()