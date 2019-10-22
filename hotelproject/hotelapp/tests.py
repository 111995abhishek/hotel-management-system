from django.test import TestCase
from .models import Hotel,Rooms,Bookings

class HotelTestCase(TestCase):
    def setUp(self):
        hotel=Hotel.objects.create(hotel_name='novotel',)
    def test_case_check_hotel_name(self):
        hotel=Hotel.objects.get(hotel_name='novotel',)

class RoomsTestcase(TestCase):
    rooms=Rooms.objects.create(room_type='Deluxe',room_no='price',Price='5000',no_of_members='2')



