from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=30)
	kf_member= models.IntegerFeld()
	is_lounge = models.BooleanField(default=False)
	is_shower = models.BooleanField(default=False)

class Lounge(models.Model):
	name = models.CharField(max_length=30)

class ShowerStall(model.Models):
	lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE)
	is_vacant = models.BooleanField(default=True)
