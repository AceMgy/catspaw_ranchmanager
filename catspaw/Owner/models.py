from django.db import models

# Create your models here.


class Phone(models.Model):
    """ Contains a single phone number and what type it is. """
    categories = ((1, "home"), (2, "work"), (3, "fax"), (4, "cell"), (5, "other"))
    phone_cat = models.IntegerField(choices=categories)
    phone_num = models.PositiveIntegerField(unique=True)

class Address(models.Model):
    """ Contains information on a single address """
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()

class Owner(models.Model):
    """ Contains information on an owner, be it an individual or company."""
    phones = models.ManyToManyField(Phone)
    address = models.ForeignKey(Address, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

class Person(Owner):
    """ Contains specific information on an individual."""
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

class Company(Owner):
    """ Contains specific information on a company. """
    name = models.CharField(max_length=50, unique=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    people = models.ManyToManyField(Person)

class Brand(models.Model):
    """ Information on a brand's characteristics and its owner. """
    owner = models.ForeignKey(Owner, null=True, blank=True)
    brand_id = models.CharField(max_length=50, unique=True)
    brand_loc = models.CharField(max_length=50, null=True, blank=True)

    # Waddles, earmarks, and other types of identification marks
    other_id = models.CharField(max_length=50, null=True, blank=True)
