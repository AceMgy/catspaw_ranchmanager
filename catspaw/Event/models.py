from django.db import models

from Owner.models import Owner
from Location.models import Ranch, AnimalLocation
# Create your models here.



""" =============General Events============= """

class Event(models.Model):
    """
    Any event that happens to a paticular animal or group of animals.
    Subcategories include Health, Medical, and user-defined events.
    """

    # Date the event happened
    date = models.DateTimeField()
    # Date this table was initially added or modified
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Additional comments
    comments = models.CharField(max_length=200, null=True, blank=True)

class CustomCategories(models.Model):
    """ A custom category for a user-defined event. """
    name = models.CharField(max_length=50, unique=True)

class CustomEvent(Event):
    """ A custom event using a user-defined category. """
    # May make this into a scriptable model if I want to get really fancy.
    category = models.ForeignKey(CustomCategories)
    attributes = models.CharField(max_length=100)
    end_date = models.DateTimeField(null=True, blank=True)
    people = models.ManyToManyField(Owner)
    ranch = models.ManyToManyField(Ranch)
    locations = models.ManyToManyField(AnimalLocation)

class Sale(Event):
    """ Sale of an animal or gametes. """
    prev_owner = models.ForeignKey(Owner, related_name="sale_prev_owner")
    new_owner = models.ForeignKey(Owner, related_name="sale_new_owner")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)



""" =============Medical events============= """

class MedicalEvent(Event):
    """
    Any event that involves treating or handling an animal or group
    of animals.
    """
    caregivers = models.ManyToManyField(Owner)
    cost = models.DecimalField(
                max_digits=12,
                decimal_places=2,
                null=True,
                blank=True,
    )

class CategoriesMedical(models.Model):
    """ All the user-defined medical event categories. """
    name = models.CharField(max_length=50, unique=True)

class CustomMedical(MedicalEvent):
    """ A medical event under a user-defined category. """
    category = models.ForeignKey(CategoriesMedical)
    attributes = models.CharField(max_length=100)
    end_date = models.DateTimeField(null=True, blank=True)
    people = models.ManyToManyField(Owner)
    ranch = models.ManyToManyField(Ranch)
    locations = models.ManyToManyField(AnimalLocation)

class AI(MedicalEvent):
    """ An event where an animal is artificially inseminated. """
    # A bunch of foreignkeys link here, placeholder for now

class PregCheck(MedicalEvent):
    """ Preg-checking a cow. """
    months_remaining = models.DecimalField(max_digits=3, decimal_places=2)
    cow_open = models.BooleanField(default=False)

class Ultrasound(MedicalEvent):
    """ Checking a pregnancy through an ultrasound. """
    months_remaining = models.DecimalField(max_digits=3, decimal_places=2)
    cow_open = models.BooleanField(default=False)
    sex_choices = ((1, "male"), (2, "female"))
    sex = models.IntegerField(choices=sex_choices, null=True, blank=True)
    # Room here to add an image file if needed

class SemenCollection(MedicalEvent):
    """ Collecting semen from a bull. """
    # Placeholder class for now, add more fields later

class EmbryoCollection(MedicalEvent):
    """ Collecting Embryos from a cow. """
    # Number of embyros recovered.
    embryo_num = models.PositiveIntegerField()



""" =============Health Events============= """

class HealthEvent(Event):
    """ Any health event (i.e. illness, birth, death) that happens
    to one or more animals. """
    severity_choices = (
                (1, "negligible"),
                (2, "significant"),
                (3, "moderate"),
                (4, "dangerous"),
                (5, "severe")
    )
    severity = models.IntegerField(
                choices=severity_choices,
                null=True,
                blank=True,
    )
    end_date = models.DateTimeField(null=True, blank=True)

    # All the medical events that are related to this health event
    treatments = models.ManyToManyField(MedicalEvent)

class Birth(HealthEvent):
    """ Birth of an animal. """
    difficulty_rating = (
                (1, "no assistance"),
                (2, "easily pulled"),
                (3, "pulled"),
                (4, "pulled with difficulty"),
                (5, "cesarean"),
    )
    calving_ease = models.IntegerField(
                        choices=difficulty_rating,
                        null=True,
                        blank=True,
    )
    live = models.BooleanField(default=True)

class Death(HealthEvent):
    """ Death of an animal. """
    # Placeholder. Add more fields later
