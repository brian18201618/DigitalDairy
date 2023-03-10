import django.forms as forms
from .models import  UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('phone_number', 'client_address', 'farm_name', 'farm_location')
