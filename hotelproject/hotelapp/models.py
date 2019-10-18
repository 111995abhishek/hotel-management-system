from django.db import models
from django import *
from django.db.models import CASCADE,DO_NOTHING
class Hotel(models.Model):
    hotel_name=models.CharField(max_length=200)

    def __str__(self):
        return self.hotel_name

class Rooms(models.Model):
    room_type=models.CharField(max_length=200,null=True)
    room_no=models.IntegerField()
    price=models.IntegerField()
    no_of_members=models.IntegerField()

    def __str__(self):
        return str(self.room_type)+""+str(self.room_no)+""+""+str(self.price)


class Manager(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Guest(models.Model):
    guest_name=models.CharField(max_length=200)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)


    def __str__(self):
        return self.guest_name



class Bookings(models.Model):
    manager_name=models.ForeignKey(Manager,on_delete=models.DO_NOTHING,null=True)
    guest_name=models.ForeignKey(Guest,on_delete=models.DO_NOTHING)
    room_no=models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    check_in=models.DateField()
    check_out=models.DateField()

    def __str__(self):
        return self.check_in+""+self.check_out






