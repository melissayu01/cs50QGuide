from django.db import models

# Create your models here.

class User(authmodels.User):
    zip_code = lfmodels.USZipCodeField()
    prof_pic = models.ImageField(upload_to=rename_file, max_length=300)

class Club(models.Model)
    name = models.CharField(max_length=30)
    description = 
    genre =
    rating = 
    
class Reviews(models.Model)
    name = models.CharField(max_length=30)
    reviews =