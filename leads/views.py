from django.shortcuts import render
from django.http import HttpResponse
from .models import Leads

# Create your views here.

##create function homepage
def home_page(request):
   # return HttpResponse('Welcome to Sales')
   leads = Leads.objects.all()
   context ={
    "leads":leads
   }
   return render(request ,"leads/home_page.html",context )
