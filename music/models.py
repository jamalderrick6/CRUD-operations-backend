from django.db import models
from django.db.models.indexes import Index


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    ratings = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.artist)

