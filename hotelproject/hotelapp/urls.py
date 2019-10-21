from django.urls import  path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()

router.register('Hotels',views.HotelView)

router.register('Rooms',views.RoomsView)

router.register('manager',views.ManagerView)

router.register('Guest',views.GuestView)

router.register('Bookings',views.BookingsView)

urlpatterns= [
    path('',include(router.urls))

]
