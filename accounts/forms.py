from django import forms    
from .models import User

class UserRegistration(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

   
    class Meta:
        model = User
        fields = [
            'firstname','lastname','username','email','phone_number','password'
        ]
        
