from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(primary_key=True,max_length=100)
	password = models.CharField(max_length = 100)
	mobile = models.IntegerField()
	address = models.CharField(max_length=100)
	email = models.EmailField(max_length=100,blank=False)
	age = models.IntegerField()

	