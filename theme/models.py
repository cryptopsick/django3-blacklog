from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Country(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return "%s" % (self.name)

class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return "%s" % (self.name)


class Band(models.Model):
    name = models.CharField(max_length=200)
    band_photo = models.ImageField(upload_to='reviews/images',blank = True)
    logo = models.ImageField(upload_to='reviews/images',blank = True)
    url = models.URLField(blank = True)
    fcbk = models.URLField(blank = True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)



class Album(models.Model):
    title = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=250,blank = True)
    image = models.ImageField(upload_to='reviews/images',blank = True)
    # score = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s by %s" % (self.title, self.band)
    
    def get_score(self):
        return score



