from django.db import models
class users(models.Model):
	name=models.CharField(max_length=15)
	email=models.CharField(max_length=35)
	gender=models.CharField(max_length=6)
	DOB=models.DateField(auto_now=False, auto_now_add=False)
	password=models.CharField(max_length=16)

