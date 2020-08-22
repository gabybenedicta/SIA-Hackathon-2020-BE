from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=30)
	kf_member= models.IntegerField()
	is_lounge = models.BooleanField(default=False)
	is_shower = models.BooleanField(default=False)

class Lounge(models.Model):
	name = models.CharField(max_length=30)

class ShowerStall(models.Model):
	lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE)
	is_vacant = models.BooleanField(default=True)
	user_id = models.IntegerField(default=None)

class ShowerQueue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	datetime = models.DateTimeField()
