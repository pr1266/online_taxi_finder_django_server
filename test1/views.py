from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView
from .models import *
from .serializer import *
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes , api_view
from django.http import JsonResponse , HttpResponse
from .forms import *
from django.shortcuts import render
from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect
from rest_framework.permissions import(
    AllowAny ,
    IsAuthenticated ,
    IsAdminUser ,
    IsAuthenticatedOrReadOnly ,
)
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from django.core import serializers
from rest_framework.filters import(
    SearchFilter ,
    OrderingFilter ,
)




# PASSENGER
class PassengerListApiView(ListAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['user', ]


class PassengerDetailApiView(RetrieveAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['user', ]
    lookup_url_kwarg = 'user'

class PassengerDeleteApiView(DestroyAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['user', ]
    lookup_url_kwarg = 'user'

class PassengerUpdateApiView(UpdateAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['user__username', ]
    lookup_url_kwarg = 'user__username'

class PassengerDetailApiView(RetrieveAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'user__username'
    lookup_url_kwarg = 'user__username'


class PassengerCreateApiView(CreateAPIView):

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

# DRIVER
class DriverListApiView(ListAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', ]


class DriverDetailApiView(RetrieveAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'user__username'
    lookup_url_kwarg = 'user__username'

class DriverUpdateApiView(UpdateAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id','user_username']
    lookup_url_kwarg = 'user__username'


class DriverDeleteApiView(DestroyAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'phone_number'
    lookup_url_kwarg = 'phone_number'

class DriverCreateApiView(CreateAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

#TRAVEL

class TravelListApiView(ListAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = 'id'


class TravelDetailApiView(RetrieveAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id', ]
    lookup_url_kwarg = 'id'

class TravelDeleteApiView(DestroyAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['passenger__id', 'driver__id']
    lookup_url_kwarg = 'id'

class TravelCreateApiView(CreateAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated]

class TravelUpdateApiView(UpdateAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['passenger__id', 'driver__id']
    lookup_url_kwarg = 'id'

# CAR
class CarListApiView(ListAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', 'license', 'driver__id']


class CarDetailApiView(RetrieveAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['license', 'driver__id']
    lookup_url_kwarg = ['license', 'driver__id']

class CarDeleteApiView(DestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['license', 'driver__id']
    lookup_url_kwarg = ['license', 'driver__id']

class CarCreateApiView(CreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

# Offer
class OfferListApiView(ListAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id']


class OfferDetailApiView(RetrieveAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id']
    lookup_url_kwarg = ['id']

class OfferDeleteApiView(DestroyAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id']
    lookup_url_kwarg = ['id']

class OfferCreateApiView(CreateAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

# City

class CityListApiView(ListAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', 'city_name']


class CityDetailApiView(RetrieveAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'city_name'
    lookup_url_kwarg = 'city_name'

    def get_queryset(self):
        city = self.kwargs['city_name']
        print(city)
        return City.objects.filter(city_name = city)

class CityDeleteApiView(DestroyAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id', 'city_name']
    lookup_url_kwarg = ['id', 'city_name']

class CityCreateApiView(CreateAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

# Location
class LocationUpdateApiView(UpdateAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id', ]
    lookup_url_kwarg = 'id'

class LocationListApiView(ListAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', 'place_name', 'city__city_name']


class LocationDetailApiView(RetrieveAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id', 'place_name', 'city__city_name']
    lookup_url_kwarg = 'place_name'

class LocationDeleteApiView(DestroyAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['id', 'place_name', 'city__city_name']
    lookup_url_kwarg = ['id', 'place_name', 'city__city_name']

class LocationCreateApiView(CreateAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

# User
class UserListApiView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', 'username']


class UserDetailApiView(RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'username'
    lookup_url_kwarg = 'username'

class UserDeleteApiView(DestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'username'
    lookup_url_kwarg = 'username'

class UserCreateApiView(CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserUpdateApiView(UpdateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['username', ]
    lookup_url_kwarg = 'username'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

# Common Place
class CommonPlaceListApiView(ListAPIView):

    queryset = Common.objects.all()
    serializer_class = CommonPlaceSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['passenger', ]


class CommonPlaceDetailApiView(RetrieveAPIView):

    queryset = Common.objects.all()
    serializer_class = CommonPlaceSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['passenger', ]
    lookup_url_kwarg = 'passenger'

class CommonPlaceDeleteApiView(DestroyAPIView):

    queryset = Common.objects.all()
    serializer_class = CommonPlaceSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['passenger', ]
    lookup_url_kwarg = 'passenger'

class CommonPlaceCreateApiView(CreateAPIView):

    queryset = Common.objects.all()
    serializer_class = CommonPlaceSerializer
    permission_classes = [IsAuthenticated]

class CommonPlaceUpdateApiView(UpdateAPIView):

    queryset = Common.objects.all()
    serializer_class = CommonPlaceSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['passenger', ]
    lookup_url_kwarg = 'passenger'

# Vote


###########
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_common(request):
    
    id = request.data['id']
    obj = Common.objects.filter(passenger = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_location(request):
    
    id = request.data['name']
    obj = Location.objects.filter(place_name = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_location_2(request):
    
    id = request.data['name']
    obj = Location.objects.filter(id = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_passenger(request):
    user_name = request.data['username']
    obj = Passenger.objects.filter(user__username = username)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_travel_passenger(request):
    
    id = request.data['id']
    obj = Travel.objects.filter(passenger = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def travel_count_passenger(request):

    id = request.data['id']
    obj = Travel.objects.filter(Q(passenger = id) & Q(end = True)).count()
    
    return JsonResponse({'result': obj}, safe = False)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def travel_count_driver(request):

    id = request.data['id']
    obj = Travel.objects.filter(Q(driver = id) & Q(end = True)).count()
    return JsonResponse({'result': obj}, safe = False)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_travel_driver(request):

    id = request.data['id']
    obj = Travel.objects.filter(driver = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_car(request):

    id = request.data['id']
    obj = Car.objects.filter(owner = id)
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_travel_city(request):

    id = request.data['id']
    obj = Travel.objects.filter(Q(city = id) & Q(end = False) & Q(accepted = False))
    serialized_obj = serializers.serialize('json', obj)
    return HttpResponse(serialized_obj, content_type = 'application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def vote(request):

    id = request.data['id']
    """obj = Vote.objects.filter(user = id)
    
    sum_ = 0

    for i in obj:
        sum_ += i.number
    
    if obj.count() != 0:
        result = float(sum_/obj.count())
        
        return JsonResponse({'result': result}, safe = False)

    else:
        return JsonResponse({'result': 0}, safe = False)"""

    pass 