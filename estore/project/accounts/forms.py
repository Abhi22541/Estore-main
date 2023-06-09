from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Userbase

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

class RegistrationForm(forms.ModelForm):
     
     user_name=forms.CharField(label='Enter Username',min_length=4, max_length=50, help_text='Required')
     email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
     password = forms.CharField(label='Password', widget=forms.PasswordInput)
     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

     class Meta:
          model=Userbase
          fields={'user_name', 'email'}
     
     
     
     def clean_user_name(self):
          user_name=self.cleaned_data['user_name'].lower()
          r=Userbase.objects.filter(user_name=user_name)
          if r.count():
               raise forms.ValidationError("USername already exists")
          return user_name
     
     def clean_password2(self):
          cd=self.cleaned_data
          if cd['password']!= cd['password2']:
               raise forms.ValidationError("Password does not match")
          return cd['password2']
     
     def clean_email(self):
          email=self.cleaned_data['email']
          if Userbase.objects.filter(email=email).exists():
               raise forms.ValidationError("Email already exists")
          return email
     
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
        

class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = Userbase
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True


# class Userform(UserCreationForm):
#     email=forms.EmailField(required=True)
#     class Meta:
#         model=User
#         fields=('username', 'email', 'password', 'password2')

#     def save(self, commit=True):
#                 user = super(Userform, self).save(commit=False)
#                 user.email = self.cleaned_data['email']
#                 if commit:
#                        user.save()
#                 return user
