from django.urls import path
from . import views

urlpatterns = [
    path('process_barcode/<int:pk>', views.process_barcode),
]