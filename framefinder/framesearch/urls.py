from django.urls import path
from . import views

urlpatterns = [
    path('', views.frame_home, name="frame_home"),
    path('search/<int:height>/<int:discipline>/<int:price>/<str:order_by>/', views.frame_search, name="frame_search"),
]