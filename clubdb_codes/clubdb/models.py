# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class club(models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=100)
    club_email = models.CharField(max_length=100)
  
    class Meta:
        managed = False
        db_table = 'club'


class events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_duration = models.IntegerField()
    event_name = models.CharField(max_length=100)
    # event date is a date field
    event_date = models.DateField()
    event_theme = models.CharField(max_length=100)
    event_capacity = models.IntegerField()
    event_eligibility = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'event_details'

 

class club_address(models.Model):
    club_id = models.IntegerField(primary_key=True)
    pincode = models.IntegerField()
    city_name = models.CharField(max_length=100)
    stat = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'club_address'