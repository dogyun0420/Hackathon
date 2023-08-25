import requests
import json
import schedule
import time
from django.shortcuts import render
from django.http import JsonResponse

def fetch_and_save_data():
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

    print(f"일련번호: {now_tmSeq}")
    print(f"일련번호: {past_tmSeq}")
#    if past_tmSeq != now_tmSeq:
        #지진 발생
#    else:
        #괜춘
    

def main_app(request):
    # 1분마다 fetch_and_save_data 함수를 실행
    # schedule.every(60).seconds.do(fetch_and_save_data)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    return render(request,"main.html")