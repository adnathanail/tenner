from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
