import requests
from django.shortcuts import render
from django.http import JsonResponse

def get_nearest_shelter(start_lat, start_lng):
    api_key = "API-KEY"
    base_url = "https://apis.openapi.sk.com/tmap/pois"

    params = {
        "version": 1,
        "format": "json",
        "appKey": api_key,
        "centerLon": start_lng,
        "centerLat": start_lat,
        "count": 1,  # 가장 가까운 1개의 결과만 요청
        "radius": 5000,  # 검색 반경 (5km)
        "page": 1
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "searchPoiInfo" in data and "pois" in data["searchPoiInfo"]:
        pois = data["searchPoiInfo"]["pois"]
        if pois:
            nearest_shelter = pois[0]
            shelter_name = nearest_shelter["name"]
            shelter_address = nearest_shelter["upperAddrName"] + " " + nearest_shelter["middleAddrName"]
            return shelter_name, shelter_address
    return None, None

def show_map(request):
    # 사용자의 위치 (예: 서울)
    user_lat = 37.5665
    user_lng = 126.9780

    # 가장 가까운 옥외대피소 정보 가져오기
    nearest_shelter_name, nearest_shelter_address = get_nearest_shelter(user_lat, user_lng)

    context = {
        "user_lat": user_lat,
        "user_lng": user_lng,
        "nearest_shelter_name": nearest_shelter_name,
        "nearest_shelter_address": nearest_shelter_address,
    }
    return render(request, "map.html", context)
