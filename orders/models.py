# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from datetime import datetime

class Item(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.name + ' - £' + str(self.price)

class OrderItem(models.Model):
    orderer = models.ForeignKey('auth.User', null=True)
    item = models.ForeignKey(Item, null=True)
    quantity = models.IntegerField( default=0)

    def __str__(self):
        return str(self.quantity) + "x " + self.item.name
