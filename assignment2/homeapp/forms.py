from django import forms
from .models import users
class userform(forms.ModelForm):
	class Meta:
		model=users
		fields=['name','email','gender','DOB','password']