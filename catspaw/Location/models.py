from django.db import models

from Owner.models import Owner, Phone, Address

# Create your models here.


class Ranch(models.Model):
    """ Information on a specific ranch. """
    name = models.CharField(max_length=50, unique=True)
    owners = models.ManyToManyField(Owner)
    phones = models.ManyToManyField(Phone)
    address = models.ForeignKey(Address, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    website = models.CharField(max_length=50)

class Pen(models.Model):
    """ Top hierarchy of a location. This could be a barn, field, pen, ect. """
    ranch = models.ForeignKey(Ranch)
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50, null=True, blank=True)

class Lot(models.Model):
    """
    Lower hierarchy of a location. This could be stalls in a barn,
    lots in a sale, ect.
    """
    pen = models.ForeignKey(Pen)
    name = models.CharField(max_length=50, null=True, blank=True)
    number = models.PositiveIntegerField(unique=True)
    location = models.CharField(max_length=50)

class AnimalLocation(models.Model):
    """ Location of a specific animal. Only field required is a ranch. """
    ranch = models.ForeignKey(Ranch)
    pen = models.ForeignKey(Pen, null=True, blank=True)
    lot = models.ForeignKey(Lot, null=True, blank=True)
