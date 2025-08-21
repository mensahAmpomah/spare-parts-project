from django import forms    
from .models import User, UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistration(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'firstname','lastname','username','email','phone_number','password'
        ]

    def clean_passwrod(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_pasword']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['confirm_password']



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'firstname','lastname','username'
        ]

# This will be used to changed the userProfile settings

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'firstname','lastname','phone_number','profile_pic','city'
        ]