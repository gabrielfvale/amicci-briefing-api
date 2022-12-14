from django.db import models
from django.contrib.postgres.fields import ArrayField


class Briefing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    retailer = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    available = models.PositiveSmallIntegerField()


class Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    retailer = ArrayField(models.IntegerField())


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
