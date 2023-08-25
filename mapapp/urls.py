from django.urls import path
from . import views, views1


urlpatterns = [
    path('show_map/', views.show_map, name='show_map'),  # 맵 보여주는 뷰
    path('tmap/', views1.map_view, name='map_view'),
]
