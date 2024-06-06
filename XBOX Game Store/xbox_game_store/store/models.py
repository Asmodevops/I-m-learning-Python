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


class CarouselItem(models.Model):
    big_image = models.ImageField(upload_to='carousel/')
    caption = models.CharField(max_length=100)
    game1 = models.ForeignKey(Game, related_name='carousel_game1', on_delete=models.CASCADE)
    small_image2 = models.ImageField(upload_to='carousel/', null=True, blank=True)
    game2 = models.ForeignKey(Game, related_name='carousel_game2', on_delete=models.CASCADE, null=True, blank=True)
    small_image3 = models.ImageField(upload_to='carousel/', null=True, blank=True)
    game3 = models.ForeignKey(Game, related_name='carousel_game3', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Carousel Item {self.id}"

class News(models.Model):
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class GamePass(models.Model):
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title