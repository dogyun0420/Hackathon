from django.shortcuts import render

def map_view(request):
    user_lat = 37.564991 
    user_lng = 126.983937
    end_lat = 37.565018
    end_lng = 126.988173
    return render(request, 'tmap.html', {'user_lat': user_lat, 
                                         'user_lng': user_lng, 
                                         'end_lat': end_lat,
                                         'end_lng':end_lng
                                         })
