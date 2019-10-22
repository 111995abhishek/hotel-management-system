from django.contrib import admin
from .models import *
from django import forms

class HotelAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(HotelAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name=self.cleaned_data.get('hotel_name')
        if len(name)>20:
            raise forms.ValidationError('name is too big',code='error')
        return self.cleaned_data

    def save(self,commit=True):
        return super(HotelAdminForm,self).save(commit=commit)

class RoomsAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs) :
        super(RoomsAdminForm, self).__init__(*args,**kwargs)

    def clean(self):
        member=self.cleaned_data.get('no_of_members')
        if member>4:
            raise forms.ValidationError('number of members exceeds the maximum limit',code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(RoomsAdminForm,self).save(commit=commit)



class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name',)
    form = HotelAdminForm

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_type','room_no','price','no_of_members',)
    form = RoomsAdminForm
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


