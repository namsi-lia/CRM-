from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

##create function homepage
def home_page(request):
   # return HttpResponse('Welcome to Sales')
   return render(request ,"leads/home_page.html")
