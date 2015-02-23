from django.db import models

IMAGE_TYPE = (
                 ('fanart', 'Fan Art'),
                 ('boxart', 'Box Art'),
                 ('banner', 'Banner'),
                 ('screenshot', 'Screen Shot'),
                 ('clearlogo', 'Clear Logo'),
             )


class PlatformManager(models.Manager):
    pass


class Platform(models.Model):
    objects = PlatformManager()
    name = models.CharField(max_length=200)


class GenreManager(models.Manager):
    pass


class Genre(models.Model):
    objects = GenreManager()
    name = models.CharField(max_length=200)


class Image(models.Model):
    image_type = models.CharField(choices=IMAGE_TYPE, max_length=50)
    url = models.URLField(max_length=200)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    thumb = models.URLField(max_length=200, null=True, blank=True)
    side = models.CharField(max_length=100, null=True, blank=True)


class GameManager(models.Manager):
    pass


class Game(models.Model):
    objects = GameManager()
    title = models.CharField(max_length=200)
    game_id = models.CharField(max_length=10, blank=True, null=True)
    platform = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.CharField(max_length=50, null=True, blank=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    # players = models.CharField(max_length=10, blank=True, null=True)
    # coop = models.CharField(max_length=10, blank=True, null=True)
    # youtube = models.URLField(max_length=200, blank=True, null=True)
    # publisher = models.CharField(max_length=200, blank=True, null=True)
    # developer = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    # images = models.ManyToManyField(Image, null=True, blank=True)
    cover_image = models.CharField(max_length=200, blank=True, null=True)


# class 
