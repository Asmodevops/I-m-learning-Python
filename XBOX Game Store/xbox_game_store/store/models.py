from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    publisher = models.CharField(max_length=200)
    features = models.ManyToManyField(Feature)
    banner_image = models.ImageField(upload_to='game_banners/', default='no_photo.jpg')

    def __str__(self):
        return self.title
