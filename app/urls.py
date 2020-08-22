from django.urls import path
from . import views

urlpatterns = [
    path('process_barcode/<int:pk>', views.process_barcode),
    path('get_queue_status/<int:pk>' views.get_queue_status),
]