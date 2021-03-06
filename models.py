# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Albums(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'

class Genre(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Libruary(models.Model):
    track_no = models.IntegerField(blank=True, null=True)
    track_name = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=80, blank=True, null=True)
    album = models.CharField(max_length=80, blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'libruary'
