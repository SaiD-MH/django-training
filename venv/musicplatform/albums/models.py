from email.policy import default
from django.db import models
from datetime import datetime

from artists.models import Artist

# Create your models here.


class Album(models.Model):
    artistName = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, default='New Album', blank=True)
    creationTime = models.DateTimeField(default=datetime.now)
    release = models.DateTimeField(
        default=datetime.now, null=False, blank=True)
    cost = models.DecimalField(
        max_digits=10, decimal_places=3, blank=False, null=False)
    # = models.IntegerField()

    def __str__(self):
        return self.name
