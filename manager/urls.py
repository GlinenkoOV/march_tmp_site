from django.urls import path
from .views import reservation_list, update_reservation

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservations'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reservation'),
]