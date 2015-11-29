from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
	category = models.CharField(max_length=30) # predefined list?

class Club(models.Model):
	name = models.CharField(max_length=30)
	abbreviation = models.CharField(max_length=10, blank=True)
	genre = models.ManyToManyField(Genre)
	description = models.TextField(max_length=2000)
	website = models.URLField(blank=True)
	overall_rating = models.DecimalField(max_digits=2, decimal_places=1, 
		null=True) # add 1-5 ratings later

class Review(models.Model):
	name = models.ForeignKey(Club)
	reviewer = models.ForeignKey(User)
	timestamp = models.DateField(auto_now_add=True)
	rating = models.PositiveSmallIntegerField(null=True)
	review = models.TextField(max_length=2000)
