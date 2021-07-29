from django.db import models

# Create your models here.
class show(models.Model):
    custname=models.CharField(max_length=50)
    vechtype=models.CharField(max_length=50)
    vechnum=models.IntegerField()
    servicetype=models.CharField(max_length=50)