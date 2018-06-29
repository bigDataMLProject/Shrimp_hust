# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    m_id = models.CharField(primary_key=True, max_length=10)
    m_name = models.CharField(max_length=40)
    rate = models.IntegerField()
    director = models.CharField(max_length=50, blank=True, null=True)
    screenwriter = models.CharField(max_length=50, blank=True, null=True)
    actor = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    imgurl = models.CharField(max_length=100, blank=True, null=True)
    star = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class Rating(models.Model):
    u_id = models.CharField(max_length=32)
    m_id = models.CharField(max_length=10)
    type = models.CharField(max_length=50, blank=True, null=True)
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rating'


class RecommendMovie(models.Model):
    m_id = models.CharField(primary_key=True, max_length=100)
    recommend_movie_id = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'recommend_movie'


class User(models.Model):
    u_id = models.CharField(primary_key=True, max_length=32)
    u_passwd = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
