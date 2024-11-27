from django.db import models


class MicroVsPlants(models.Model):
    plant = models.ForeignKey('Plants', models.DO_NOTHING, blank=True, null=True)
    micro = models.ForeignKey('Microorganisms', models.DO_NOTHING, blank=True, null=True)
    publication = models.ForeignKey('Publications', models.DO_NOTHING, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    concentration_sd = models.FloatField(blank=True, null=True)
    concentration_se = models.FloatField(blank=True, null=True)
    concentration_units = models.CharField(max_length=255, blank=True, null=True)
    repetitions = models.IntegerField(blank=True, null=True)
    experiment_type = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.CharField(max_length=63, blank=True, null=True)
    sd = models.FloatField(blank=True, null=True)
    se = models.FloatField(blank=True, null=True)
    units = models.CharField(max_length=255, blank=True, null=True)
    interpretation_value = models.FloatField(blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)
    method_name = models.CharField(max_length=255, blank=True, null=True)
    method_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'micro_vs_plants'


class Microorganisms(models.Model):
    name = models.CharField(max_length=255)
    name_alt = models.CharField(max_length=255, blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microorganisms'


class Plants(models.Model):
    common_name = models.CharField(max_length=255, blank=True, null=True)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    part = models.CharField(max_length=63, blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants'


class Publications(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    publication_year = models.SmallIntegerField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publications'