from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30)
	description = models.TextField(max_length=2000)
	# ratings?

class Review(models.Model):
	name = models.ForeignKey(Club)
	reviewer = models.ForeignKey(User)
	review = models.TextField(max_length=2000)
	date_time = models.DateTimeField()

