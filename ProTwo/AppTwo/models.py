from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank= True)
	profile_pics = models.ImageField(upload_to = 'profile_pics', blank = True)

	def __str__(self):
		return self.user.username



class Meal1(models.Model):
	username = models.CharField(max_length = 30, null = True)
	breakfast_meal = models.PositiveIntegerField(default=True)
	lunch_meal = models.PositiveIntegerField(default=True)
	dinner_meal = models.PositiveIntegerField(default=True)

	def __str__(self):
		return self.username


class FreeMeal(models.Model):
	username = models.CharField(max_length = 30, null = True)
	breakfast_meal = models.PositiveIntegerField(default=True)
	lunch_meal = models.PositiveIntegerField(default=True)
	dinner_meal = models.PositiveIntegerField(default=True)

	def __str__(self):
		return self.username
