from django.urls import path
from . import views, views1, views2

urlpatterns = [
    path('', views2.main_app, name='main_app'),
    path('map_view/', views.map_view, name='map_view'),  # 맵 보여주는 뷰
    path('tmap/', views1.map_view, name='map_view'),
]
