from django import forms

class ImgForm(forms.Form):
    myimage=forms.ImageField(required=False)