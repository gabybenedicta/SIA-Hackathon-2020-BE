from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import User


@api_view(['POST'])
def process_barcode(request, pk):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            message = "User does not exist"
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        print("USER")
        print(user)

        if request.data["barcodeValue"] == "123457629":
            returned = "Showers"
            return Response(returned, status = status.HTTP_200_OK)
        elif request.data["barcodeValue"] == "9189283746":
            returned = "Services"
            return Response(returned, status = status.HTTP_200_OK)
        return Response("Not Found", status= status.HTTP_404_NOT_FOUND)