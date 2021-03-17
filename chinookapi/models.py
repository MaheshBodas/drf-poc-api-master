# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Generate tokens for every user upon save
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actors'


class Album(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        db_table = 'albums'

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'artists'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'categories'


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60)
    support_rep = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'customers'


class Employee(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True, null=True)
    reports_to = models.ForeignKey('self', on_delete=models.CASCADE, db_column='reports_to', blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    hire_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'employees'


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language_id = models.SmallIntegerField()
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'films'


class Genre(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class MediaType(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'media_types'

    def __str__(self):
        return self.name


class PlaylistTrack(models.Model):
    playlist = models.OneToOneField('Playlist', models.DO_NOTHING, primary_key=True)
    track = models.ForeignKey('Track', on_delete=models.CASCADE)

    class Meta:
        db_table = 'playlist_track'
        unique_together = (('playlist', 'track'),)


class Playlist(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'playlists'


class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    composer = models.CharField(max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tracks'

    def __str__(self):
        return self.name
