from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput, strip=False)
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput, strip=False)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "password_confirm")
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password_confirm != password:
            raise forms.ValidationError

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user
