from email.policy import default
from django.db import models
from datetime import datetime

from artists.models import Artist

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=60, default='New Album')
    artistName = models.ForeignKey(Artist, on_delete=models.CASCADE)
    creationTime = models.DateTimeField(default=datetime.now)
    release = models.DateTimeField(default=datetime.now)
    cost = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    isApproved = models.BooleanField(
        default=False, help_text='Approve the album if its name is not explicit')
    # = models.IntegerField()

    def __str__(self):
        return self.name
