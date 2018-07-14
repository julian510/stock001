from django.db import models

# Create your models here.
class user(models.Model):
    nameid = models.AutoField(primary_key=True, max_length=20)
    username = models.CharField(max_length=50, unique=True, null=True)
    passwd = models.CharField(max_length=50)
    chiname = models.CharField(max_length=50)
    phnum = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=None)

class stock_data(models.Model):
    index = models.BigIntegerField(primary_key=True, null=False)
    date = models.CharField(null=False, max_length=50)
    open = models.FloatField(null=False)
    close = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    volume = models.FloatField(null=False)
    code = models.TextField(null=False)


