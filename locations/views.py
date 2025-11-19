from django.shortcuts import render

def index(request):
    return render(request, 'locations/locations.html')

def location(request):
    return render(request, 'locations/location.html')

def search(request):
    return render(request, 'locations/search.html')
