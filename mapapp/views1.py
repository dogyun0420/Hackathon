from django.shortcuts import render

def map_view(request):
    return render(request, 'tmap.html')
