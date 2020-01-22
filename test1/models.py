from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):

    username     = models.CharField(max_length = 250, primary_key = True)
    first_name   = models.CharField(max_length = 250)
    last_name    = models.CharField(max_length = 250)
    city         = models.ForeignKey('City', on_delete = models.CASCADE, null = True)
    #city = models.CharField(max_length = 30, null = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):

        return self.username

class City(models.Model):

    city_name = models.CharField(max_length = 250, primary_key = True)
    price     = models.FloatField(null = True)

    def __str__(self):

        return self.city_name

class Location(models.Model):

    place_name = models.CharField(max_length = 250)
    lat        = models.FloatField(null = True)
    lng        = models.FloatField(null = True)
    city       = models.ForeignKey(City, on_delete = models.CASCADE, null = True)

    class Meta:
        unique_together = (("place_name", "id"),)

    def __str__(self):

        return self.place_name

class Car(models.Model):
    
    license = models.CharField(max_length = 30)
    model = models.CharField(max_length = 30, null = True)
    owner = models.CharField(max_length = 30, null = True)

    def __str__(self):

        return self.model

class Driver(models.Model):

    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    balance = models.IntegerField(default = 0)
    permission = models.BooleanField(default = False)

    def __str__(self):

        return str(self.user.username)
    
        
class Offer(models.Model):

    persent = models.IntegerField(null = True)
    expire_date = models.DateField(null = True)

    def __str__(self):
        return str(self.id)

class Passenger(models.Model):

    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    offer = models.ForeignKey(Offer, on_delete = models.CASCADE, null = True)
    balance = models.FloatField(default = 0.0)
    
    def __str__(self):

        return str(self.user.username)

class Pre_Vote(models.Model):

    string = models.CharField(max_length = 100, null = True)

    def __str__(self):

        return self.string

class Passenger_vote(models.Model):

    passenger = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    pre_vote = models.ForeignKey(Pre_Vote, on_delete = models.CASCADE, null = True)
    int_vote = models.IntegerField(default = 1, null = True)
    string = models.CharField(max_length = 300, null = True)
    travel = models.ForeignKey('Travel', on_delete = models.CASCADE)

    def __str__(self):

        return self.passenger.first_name + " " + self.passenger.last_name + " " + self.travel.id

class Driver_vote(models.Model):

    driver = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    pre_vote = models.ForeignKey(Pre_Vote, on_delete = models.CASCADE, null = True)
    int_vote = models.IntegerField(default = 1, null = True)
    string = models.CharField(max_length = 300, null = True)
    travel = models.ForeignKey('Travel', on_delete = models.CASCADE)

    def __str__(self):

        return self.driver.first_name + " " + self.driver.last_name + " " + self.travel.id

class Common(models.Model):

    place = models.ForeignKey(Location, on_delete = models.CASCADE, null = True)
    passenger = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return str(self.id)

class Travel(models.Model):

    passenger = models.ForeignKey(Passenger, on_delete = models.CASCADE, null = True)
    #passenger = models.CharField(max_length = 100, null = True)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, null = True)
    #driver = models.CharField(max_length = 100, null = True)
    cost = models.FloatField(null = True)
    date = models.DateField(null = True, auto_now_add = True)
    payment_methods = [
    ('CASH', 'cash'), ('ONLINE', 'online')
    ]
    payment_status = models.CharField(choices = payment_methods, max_length = 6)
    pickup = models.ForeignKey(Location, on_delete = models.CASCADE, related_name = 'pickup_point', null = True)
    #pickup = models.CharField(null = True, max_length = 30)
    drop = models.ManyToManyField(Location, related_name = 'drop_point')
    #drop = models.CharField(null = True, max_length = 30)
    distance = models.FloatField(null = True)
    total_stop = models.FloatField(null = True)
    accepted = models.BooleanField(default = False)
    end = models.BooleanField(default = False)
    city = models.ForeignKey(City, on_delete = models.CASCADE, null = True)

    def __str__(self):

        return str(self.id)