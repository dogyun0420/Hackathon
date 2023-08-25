from django.contrib import admin
from django.urls import path, include
from mapapp import views  # 필요한 뷰 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_map, name='show_map'),  # '/' 경로에 show_map 뷰 할당
    path('map/', include('mapapp.urls')),
]
