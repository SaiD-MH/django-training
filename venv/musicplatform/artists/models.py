from django.db import models

# Create your models here.


class Artist(models.Model):

    stageName = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    socialLink = models.URLField(max_length=100, blank=True, null=False)

    class Meta:
        ordering = ['stageName']

    def __str__(self):
        return self.stageName
