from django import forms

from gallery.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = (
            "image",
            "description")
