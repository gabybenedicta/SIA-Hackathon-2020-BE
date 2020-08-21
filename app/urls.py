from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls'))
]