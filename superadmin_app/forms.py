from django import forms

from superadmin_app.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(choices=[
        (2, "admin"),
        (3, "user")
    ], widget=forms.Select)
    
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password', 'role']
        
        