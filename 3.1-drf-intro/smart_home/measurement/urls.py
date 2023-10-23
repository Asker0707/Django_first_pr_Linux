from django.urls import path
from .views import SensorCreate, SensorChange, MeasurementAdd, SensorList, SensorDetailInfo

urlpatterns = [
    path('create/', SensorCreate.as_view()),
    path('change/<pk>/', SensorChange.as_view()),
    path('measurement/', MeasurementAdd.as_view()),
    path('list/', SensorList.as_view()),
    path('detail/<pk>/', SensorDetailInfo.as_view()),
]
