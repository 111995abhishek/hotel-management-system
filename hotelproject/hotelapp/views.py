from rest_framework import viewsets
from .serializers import HotelSerializer,RoomsSerializer,ManagerSerializer,GuestSerializer,BookingsSerializer
from .models import Hotel,Rooms,Manager,Guest,Bookings
from rest_framework .response import Response
from rest_framework import generics
from rest_framework .decorators import api_view
from rest_framework import status


class HotelView(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class RoomsView(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Rooms.objects.all()

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class BookingsView(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    queryset = Bookings.objects.all()

@api_view(['GET'])
def api_hotel_list_view(request):
    hotel=Hotel.objects.all()
    if request.method=='GET':
        serializer=HotelSerializer(hotel,many=True)
    return Response(serializer.data)

@api_view(['GET'])
#127.0.0.1/hotels/1/
def api_hotel_detail_view(request, id):
    try:
        hotel=Hotel.objects.get(id=id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = HotelSerializer(hotel)
    return Response(serializer.data)

@api_view(['PUT'])
def api_update_hotel_detail_view(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = HotelSerializer(hotel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data= {}
            data['Success']='updation successful'
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def api_create_hotel_detail_view(request):

    if request.method == 'POST':
        serializer=HotelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'creation successful'
            return Response(serializer.data)

        return Response(status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def api_delete_hotel_detail_view(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='DELETE':
        operation=hotel.delete()
        data={}
        if operation:
            data['Success']='deletion successful'
        else:
            data['Failure']='deletion failed'
        return Response(data,status=status.HTTP_200_OK)

class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self,serializer):
        try:
            hotel = Hotel.objects.get(hotel_name = self.request.data['hotel_name'])

            if hotel:
                raise ValueError('Name is already exist!')


        except Hotel.DoesNotExist:
            pass
        serializer.save(hotel_name = self.request.data['hotel_name'])




    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = HotelSerializer(queryset, many=True)
    #     return Response(serializer.data)





