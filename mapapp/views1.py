from django.shortcuts import render

def map_view(request):
    context = {
        'latitude': 37.52084364186228,
        'longitude': 127.058908811749,
        'start_x': 127.02810900563199,
        'start_y': 37.519892712436906,
        'end_x': 127.11971717230388,
        'end_y': 37.49288934463672,
        'pass_list': "127.07389565460413,37.5591696189164_127.13346617572014,37.52127761904626",
        'api_key': 'YOUR_TMAP_API_KEY',  # 발급받은 TMap API 키
    }
    return render(request, 'tmap.html', context)
