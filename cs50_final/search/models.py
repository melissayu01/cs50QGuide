from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
	SCIENCE = 1
	MATH = 2
	SERVICE = 3
	PUBLICATIONS = 4
	SPORTS = 5
	FINANCE = 6
	CULTURE = 7
	DANCE = 8
	CLUB_CATEGORIES = (
		(SCIENCE, 'Science'),
		(MATH, 'Math'),
		(SERVICE, 'Service'),
		(PUBLICATIONS, 'Publications'),
		(SPORTS, 'Sports'),
		(FINANCE, 'Finance'),
		(CULTURE, 'Culture'),
		(DANCE, 'Dance'),
	)
	category = models.IntegerField(choices=CLUB_CATEGORIES)
	
	def __str__(self):
		return "%s [%s]" % (self.category, self.get_category_display())

class Club(models.Model):
	name = models.CharField(max_length=30, blank=True)
	abbreviation = models.CharField(max_length=10, blank=True)
	genre = models.ManyToManyField(Genre)
	description = models.TextField(max_length=2000)
	website = models.URLField(blank=True)
	overall_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True,
		null=True) # add 1-5 ratings later
	
	def __str__(self):
		return self.name

class Review(models.Model):
	name = models.ForeignKey(Club)
	reviewer = models.ForeignKey(User)
	timestamp = models.DateField(auto_now_add=True)
	rating = models.PositiveSmallIntegerField()
	review = models.TextField(max_length=2000)

	def __str__(self):
		return '%s: %s' % (self.reviewer, self.name)