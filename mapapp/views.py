# mapapp/views.py

import math
import requests
from django.shortcuts import render
from .models import OutdoorShelter
from django.http import JsonResponse

def get_nearest_shelter(request):
    user_latitude = float(request.GET.get('latitude'))
    user_longitude = float(request.GET.get('longitude'))
    
    print('a'+ user_latitude, user_longitude)
    nearest_shelter = find_nearest_shelters(user_latitude, user_longitude)
    
    return render(request, 'map.html', {'nearest_shelter': nearest_shelter})

def haversine(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of Earth in kilometers
    radius = 6371.0

    distance = radius * c
    return distance

def find_nearest_shelters(latitude, longitude, num_shelters=3):
    shelters = OutdoorShelter.objects.all()
    
    distances = []
    for shelter in shelters:
        shelter_distance = haversine(latitude, longitude, shelter.ycord, shelter.xcord)
        distances.append((shelter, shelter_distance))
    
    distances.sort(key=lambda x: x[1])  # Sort by distance
    nearest_shelters = [shelter for shelter, _ in distances[:num_shelters]]
    
    return nearest_shelters

# Rest of the code remains the same

def map_view(request):
    if "geolocation" in request.GET:
        user_latitude = float(request.GET.get('latitude'))
        user_longitude = float(request.GET.get('longitude'))

        nearest_shelters = find_nearest_shelters(user_latitude, user_longitude, num_shelters=3)  # 여기를 수정하여 원하는 대피소 개수로 변경
        
        shelters_data = [{
            'vt_acmdfclty_nm': shelter.vt_acmdfclty_nm,
            'dtl_adres': shelter.dtl_adres,
            'ycord': shelter.ycord,
            'xcord': shelter.xcord,
        } for shelter in nearest_shelters]
        
        data = {
            'nearest_shelters': shelters_data
        }
        
        return JsonResponse(data)  # JSON 응답 반환
    
    return render(request, 'map.html')
