from django.contrib.gis.db import models

from user.models import User


class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    geom = models.PointField(srid=4326, unique=True)
    aproved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
