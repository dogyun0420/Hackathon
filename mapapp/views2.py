import requests
import json
import schedule
import time
from django.shortcuts import render
from django.http import JsonResponse
import threading

def fetch_and_send_data():
    api_key = "-mPst9VqQ9Kj7LfVaoPS6Q"
    base_url = "https://apihub.kma.go.kr/api/typ02/openApi/EqkInfoService/getEqkMsg?pageNo=1&numOfRows=1&dataType=JSON&fromTmFc=20171101&toTmFc=20230825&authKey=-mPst9VqQ9Kj7LfVaoPS6Q"

    params = {
        "pageNo": 1,
        "numOfRows": 1,
        "dataType": "JSON",
        "fromTmFc": "20171101",
        "toTmFc": "20230825", 
        "apikey": api_key
    }

    # API 호출 및 데이터 가져오기
    response = requests.get(base_url, params=params)
    data = response.json()

    now_tmSeq = data.get('response').get('header').get('tmSeq') #발표일련번호
    past_tmSeq = now_tmSeq

    if past_tmSeq != now_tmSeq:
        tmEqk = data.get('response').get('header').get('tmEqk')
        lat= data.get('response').get('header').get('lat')
        lon= data.get('response').get('header').get('lon')
        mt= data.get('response').get('header').get('mt')
        inT= data.get('response').get('header').get('inT')

        context = {'tmSeq' : now_tmSeq, 'tmEqk' : tmEqk, 'lat' : lat, 'lon': lon, 'mt' : mt, 'inT' : inT}

        return context
    else:
        context = {'same' : 1231314}
        return  context
        

def main_app(request):
    return render(request, 'main.html', fetch_and_send_data())

def schedule_fetch_and_send_data():
    while True:
        fetch_and_send_data()
        time.sleep(60)  # 60초 = 1분

# 스레드 생성 및 시작
schedule_thread = threading.Thread(target=schedule_fetch_and_send_data)
schedule_thread.daemon = True
schedule_thread.start()