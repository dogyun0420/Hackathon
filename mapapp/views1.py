from django.shortcuts import render

def map_view(request):
    user_lat = float(request.GET.get('user_lat', 37.564991))  # Default latitude if not provided
    user_lng = float(request.GET.get('user_lng', 126.983937))  # Default longitude if not provided
    end_lat = float(request.GET.get('end_lat', 0))
    end_lng = float(request.GET.get('end_lng', 0))

    print(user_lat, end_lat)
    return render(request, 'tmap.html', {'user_lat': user_lat, 'user_lng': user_lng, 'end_lat': end_lat, 'end_lng': end_lng})
