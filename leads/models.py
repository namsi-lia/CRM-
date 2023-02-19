from django.db import models

# Create your models here.
## this is a representation of your database schema

class Leads(models.Model):
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    age =models.IntegerField(default=0)
