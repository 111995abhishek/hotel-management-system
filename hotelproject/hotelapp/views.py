from rest_framework import viewsets
from .serializers import HotelSerializer,RoomsSerializer,ManagerSerializer,GuestSerializer,BookingsSerializer
from .models import Hotel,Rooms,Manager,Guest,Bookings

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


