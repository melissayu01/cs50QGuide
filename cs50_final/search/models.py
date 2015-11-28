from django.db import models

# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30)
	description = models.TextField(max_length=2000)
	# ratings?

class Reviews(models.Model):
	name = models.ForeignKey(Club)
	review = models.TextField(max_length=2000)