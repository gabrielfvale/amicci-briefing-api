from django.db import models


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    vendors = models.ManyToManyField(Vendor, blank=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)


class Briefing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    retailer_id = models.ForeignKey(
        Retailer, on_delete=models.DO_NOTHING, serialize=False
    )
    category_id = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, serialize=False
    )
    responsible = models.CharField(max_length=200)
    release_date = models.DateField()
    available = models.PositiveSmallIntegerField()
