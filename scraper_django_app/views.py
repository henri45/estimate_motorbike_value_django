from django.shortcuts import render
import datetime

# Create your views here.

def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})
