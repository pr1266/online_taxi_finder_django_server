from .models import *
from rest_framework.serializers import ModelSerializer , SerializerMethodField , CharField , ValidationError , StringRelatedField
from django.db.models import Q

class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CommonPlaceSerializer(ModelSerializer):

    class Meta:
        model = Common
        fields = '__all__'

class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class DriverSerializer(ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

class PassengerSerializer(ModelSerializer):

    class Meta:
        model = Passenger
        fields = '__all__'

class TravelSerializer(ModelSerializer):

    class Meta:
        model = Travel
        fields = '__all__'

class OfferSerializer(ModelSerializer):

    class Meta:
        model = Offer
        fields = '__all__'

class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'