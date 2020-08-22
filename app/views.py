from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import User, ShowerQueue


@api_view(['POST'])
def process_barcode(request, pk):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            message = "User does not exist"
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        if user.is_lounge and not user.is_shower and request.data["barcodeValue"] == "123457629":
            returned = "Showers"
            return Response(returned, status = status.HTTP_200_OK)
        elif request.data["barcodeValue"] == "9189283746":
            returned = "Services"
            user.is_lounge = True
            user.save()
            return Response(returned, status = status.HTTP_200_OK)
        return Response("Not Found", status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_shower_queue()

@api_view(['POST'])
def join_shower_queue(request, pk, lounge):
    if request.method == 'POST':
        # check if there is empty stall, if yes right away allow check in
        vacant_stalls = list(ShowerStall.objects.filter(is_vacant = True))
        if len(vacant_stalls) > 0:
            

        # else put user id in queue (based on loungeID 