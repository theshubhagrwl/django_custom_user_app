from users.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=' Email ',
                            widget=forms.TextInput(attrs={
                            "placeholder":"Type Email",
                            "id":"exampleFormControlInput1",
                            "class":"form-control"
                            }))
    name = forms.CharField(required=False,
                            label=' Username ',
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Your name",
                                    "class":"form-control",
                                    "id":"name",
                                }
                            ))
    password1 = forms.CharField(required=False,
                            label='Password ',
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder":"Password",
                                    "class":"form-control",
                                    "id":"inputPassword1",
                                }
                            ))
    password2 = forms.CharField(required=False,
                            label='Confirm Password ',
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder":"Confirm Password",
                                    "class":"form-control",
                                    "id":"inputPassword2",
                                }
                            ))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
    class Meta:
      model = CustomUser
      fields = ('email','name')
    #   fields = '__all__'
