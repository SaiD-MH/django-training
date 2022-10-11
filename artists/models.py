from django.db import models

# Create your models here.


class Artist(models.Model):

    stageName = models.CharField(max_length=100, unique=True)
    socialMediaProfile = models.CharField(max_length=100)

    class Meta:
        ordering = ['stageName']

    def __str__(self):
        return self.stageName
