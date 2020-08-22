from django.urls import path
from . import views

urlpatterns = [
    path('process_barcode/<int:pk>', views.process_barcode),
    path('join_shower_queue/<int:pk>/lounge/<int:lounge>', views.join_shower_queue),
]