from django.shortcuts import render
import requests


def Calculator(request):
    rate=None
    if request.method=="POST":
        amount= float (request.POST['amount'])
        time=  float (request.POST['time'])
        rate=  float (request.POST['rate'])
        rate = (amount /100)*rate*time*12# for calculating simple interest
        rate = round(rate, 2) # for calculating simple interest
        
    
        
    
    return render(request, 'index.html', {'rate': rate})
    
