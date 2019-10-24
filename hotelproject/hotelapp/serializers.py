from rest_framework import serializers
from  .models import Hotel,Rooms,Manager,Guest,Bookings

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','hotel_name',)

class RoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rooms
        fields =('room_type','room_no','price','no_of_members')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields=('name',)

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields=('guest_name','room')

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields=('manager_name','guest_name','room_no','check_in','check_out',)



