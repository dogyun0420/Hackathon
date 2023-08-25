from django.urls import path
from . import views

urlpatterns = [
    path('show_map/', views.show_map, name='show_map'),  # 맵 보여주는 뷰
]
