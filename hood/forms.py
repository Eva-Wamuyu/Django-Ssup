
from django import forms
from .models import HoodUser,Business, Post


class RegistrationForm(forms.ModelForm):
  first_name = forms.CharField(max_length=120)
  last_name = forms.CharField(max_length=120)
  password = forms.CharField(max_length=255, widget=forms.PasswordInput())
  class Meta:
    model = HoodUser
    fields = ['first_name', 'last_name', 'email', 'password','hood' ]

    labels = {
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email Address',
      'password': 'A Strong Password'
    }

class LoginForm(forms.Form):
  email = forms.CharField(max_length=255, widget=forms.EmailInput())
  password = forms.CharField(max_length=255, widget=forms.PasswordInput())
  
  




class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ['user','avatar']

    labels = {
      'name': 'Business Name',
      'hood': 'Business Locality',
      'biz_type':'What Does it Deal with',
      'avatar': 'A business Photo can be handy Not mandatory'
    }


class AddPost(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['post']


  
class UpdateProfile(forms.ModelForm):
  class Meta:
    model = HoodUser
    fields = ['avatar','msg','hood']

    labels = {
      'avatar': 'An Image',
      'msg': 'Message/Bio',
      'hood': 'Where Do You Live'
    }

  




  


    
   

  


