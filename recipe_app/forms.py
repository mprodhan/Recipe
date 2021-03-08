from django import forms
from recipe_app.models import Food
from recipe_user.models import RecipeUser

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    ingredients = forms.CharField(widget=forms.Textarea)
    directions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=RecipeUser.objects.all())
