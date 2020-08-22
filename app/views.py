from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import User, ShowerQueue, ShowerStall


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
def get_queue_status(request, pk):
    if request.method != "GET":
        return Response("Not Found", status= status.HTTP_404_NOT_FOUND)
    #isJoined, canShower, isInShower, queueLength, stallEnter
    isJoined = False
    canShower = False
    isInShower = False
    queueLength = False
    stallEnter = None

    #get the empty stalls
    empty_stalls = list(ShowerStall.objects.filter(is_vacant=True))

    #check if user is in queue
    users_in_queue = list(ShowerQueue.objects.values_list('user_id'))
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        message = "User does not exist"
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    if user.id in queue:
        isJoined = True

    #check if user is in shower
    isInShower = user.is_shower

    #there is an empty stall
    if len(empty_stalls) == 0:
        canShower = True
        stallEnter = empty_stalls[0].id
    #not showering but in the queue
    elif(not isInShower and isJoined):
        user_queue = ShowerQueue.objects.filter(user_id = user.id)
        user_datetime = user_queue.datetime
        #get all the people in front
        queue_infront = list(ShowerQueue.objects.filter(datetime_lt=user_datetime))
        queueLength = len(queue_infront)
    else:
        queueLength = len(users_in_queue)
    response = {
        isJoined,
        isInShower,
        canShower,
        queueLength,
        stallEnter
    }
    return Response(response, status = status.HTTP_200_OK)

        
    
