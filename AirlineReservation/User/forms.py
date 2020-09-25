from django import forms
from django.contrib.auth.model import User

class UserForm(forms.modelForm):

    class Meta :
        model = User
        fields = (username, password, email)
