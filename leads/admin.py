from django.contrib import admin

from .models import User, Leads, Agent
## this imports all the models created on the models file

# Register your models here.
## register your database schema

admin.site.register(User)

