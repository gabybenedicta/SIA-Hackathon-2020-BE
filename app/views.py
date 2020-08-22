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
    queueLength = None
    stallEnter = None

    #check if user is in queue
    users_in_queue = list(ShowerQueue.objects.values_list('user_id'))
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        message = "User does not exist"
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    if user.id in users_in_queue:
        isJoined = True

    #get the assigned stalls
    assigned_stall = list(ShowerStall.objects.filter(user_id=user.id))
    if(len(assigned_stall) > 0):
        stallEnter = assigned_stall[0].id
    #check if user is in shower
    isInShower = user.is_shower
    #not showering but in the queue
    if(not isInShower and isJoined):
        user_queue = ShowerQueue.objects.filter(user_id = user.id)
        user_datetime = user_queue.datetime
        #get all the people in front
        queue_infront = list(ShowerQueue.objects.filter(datetime__lt=user_datetime))
        queueLength = len(queue_infront)
    else:
        queueLength = len(users_in_queue)
    response = {
        "isJoined": isJoined,
        "isInShower": isInShower,
        "canShower": canShower,
        "queueLength":queueLength,
        "stallEnter": stallEnter
    }
    return Response(response, status = status.HTTP_200_OK)

@api_view(["POST"])
def check_in_to_shower(request, pk):
    if request.method != "POST":
        return Response("Not Found", status= status.HTTP_404_NOT_FOUND)
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        message = "User does not exist"
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    user.is_shower = True
    user.save()

    isJoined = False
    canShower = False
    isInShower = True
    queueLength = None
    stallEnter = None

    response = {
        "isJoined": isJoined,
        "isInShower": isInShower,
        "canShower": canShower,
        "queueLength":queueLength,
        "stallEnter": stallEnter
    }
    return Response(response, status = status.HTTP_200_OK)


    
    

        
    
