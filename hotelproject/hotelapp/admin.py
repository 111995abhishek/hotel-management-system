from django.contrib import admin
from .models import *

class RoomsAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):


class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name',)

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_type','room_no','price','no_of_members',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name','room',)


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('manager_name','guest_name','room_no','check_in','check_out',)

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Rooms,RoomsAdmin)
admin.site.register(Bookings,BookingsAdmin)


