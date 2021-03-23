from django import forms

from recipe_profile.models import ProfileImage

class ImageForm(forms.Form):
    profile_image = forms.ImageField()


