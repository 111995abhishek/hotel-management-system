from django.urls import  path, include
from . import views
from .views import api_hotel_list_view, api_hotel_detail_view, api_update_hotel_detail_view, \
    api_create_hotel_detail_view, api_delete_hotel_detail_view, HotelList

#from rest_framework import routers

#router=routers.DefaultRouter()

#router.register('Hotels',views.HotelView)

#router.register('Rooms',views.RoomsView)

#router.register('manager',views.ManagerView)

#router.register('Guest',views.GuestView)

#router.register('Bookings',views.BookingsView)

urlpatterns= [
    path('hotels/',api_hotel_list_view,name='hotel'),
    path('hotels/<int:id>/',api_hotel_detail_view,name='hotel_detail'),
    path('hotels/<int:id>/update/',api_update_hotel_detail_view,name='hotel_update'),
    path('hotels/create/', api_create_hotel_detail_view,name='hotel_create'),
    path('hotels/<int:id>/delete/', api_delete_hotel_detail_view, name='hotel_delete'),


    path('hotels/generics/', HotelList.as_view(), name='hotel_generics')
]
