from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
## this is a representation of your database schema

## create a user with abstract user function which will be used by both new users and agents

class User(AbstractUser):
    pass

class Leads(models.Model):
    
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    age =models.IntegerField(default=0)
    agent =models.ForeignKey("Agent", on_delete=models.CASCADE)

 
class Agent (models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"