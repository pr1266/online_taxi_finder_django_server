from django.contrib import admin
from django.urls import path
from test1 import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api-token-auth/' , obtain_jwt_token),
    #User
    url('createuser/', views.UserCreateApiView.as_view()),
    url(r'^user/$', views.UserListApiView.as_view()),
    url(r'^user/(?P<username>[\w-]+)/$', views.UserDetailApiView.as_view()),
    url(r'^user/(?P<username>[\w-]+)/delete/$', views.UserDeleteApiView.as_view()),
    url(r'^user/(?P<username>[\w-]+)/update/$', views.UserUpdateApiView.as_view()),
    #Passenger
    url(r'^passenger/$' , views.PassengerListApiView.as_view()),
    url(r'^passenger/(?P<user__username>[\w-]+)/$' , views.PassengerDetailApiView.as_view() , name = 'detail'),
    url(r'^passenger/(?P<user__username>[\w-]+)/delete/$' , views.PassengerDeleteApiView.as_view() , name = 'delete'),
    url(r'^passenger/(?P<user__username>[\w-]+)/update/$',views.PassengerUpdateApiView.as_view()),
    url(r'createpassenger/' , views.PassengerCreateApiView.as_view() , name = 'create'),
    #CommonPlaces
    url(r'^commonplace/$' , views.CommonPlaceListApiView.as_view()),
    url(r'^commonplace/(?P<passenger>[\w-]+)/$' , views.CommonPlaceDetailApiView.as_view() , name = 'detail'),
    url(r'^commonplace/(?P<passenger>[\w-]+)/delete/$' , views.CommonPlaceDeleteApiView.as_view() , name = 'delete'),
    url(r'^commonplace/(?P<passenger>[\w-]+)/update/$',views.CommonPlaceUpdateApiView.as_view()),
    url('createcommonplace/' , views.CommonPlaceCreateApiView.as_view() , name = 'create'),
    url('get_common', views.get_common),
    #Driver
    url(r'^driver/$' , views.DriverListApiView.as_view()),
    url(r'^driver/(?P<user__username>[\w-]+)/$' , views.DriverDetailApiView.as_view() , name = 'detail'),
    url(r'^driver/(?P<user__username>[\w-]+)/delete/$' , views.DriverDeleteApiView.as_view() , name = 'delete'),
    
    url(r'^driver/(?P<user__username>[\w-]+)/update/$',views.DriverUpdateApiView.as_view()),
    
    url(r'createdriver/' , views.DriverCreateApiView.as_view() , name = 'create'),
    #Travel
    url(r'^travel/$' , views.TravelListApiView.as_view()),
    url(r'^travel/(?P<id>[\w-]+)/$' , views.TravelDetailApiView.as_view() , name = 'detail'),
    url(r'^travel/(?P<id>[\w-]+)/delete/$' , views.TravelDeleteApiView.as_view() , name = 'delete'),
    url(r'^travel/(?P<id>[\w-]+)/update/$' , views.TravelUpdateApiView.as_view() , name = 'update'),
    url(r'createtravel/' , views.TravelCreateApiView.as_view() , name = 'create'),
    #get travel
    url('get_travel_passenger/', views.get_travel_passenger),
    url('get_travel_driver/', views.get_travel_driver),
    url('travel_count_passenger/', views.travel_count_passenger),
    url('travel_count_driver/', views.travel_count_driver),
    url('get_travel_city/', views.get_travel_city),
    url('vote/', views.vote),
    #Location
    url(r'^location/$' , views.LocationListApiView.as_view()),
    url(r'^location/(?P<place_name>[\w-]+)/$' , views.LocationDetailApiView.as_view() , name = 'detail'),
    url(r'^location/(?P<place_name>[\w-]+)/delete/$' , views.LocationDeleteApiView.as_view() , name = 'delete'),
    url(r'^location/(?P<id>[\w-]+)/update/$' , views.LocationUpdateApiView.as_view() , name = 'update'),
    url(r'createlocation/' , views.LocationCreateApiView.as_view() , name = 'create'),
    #Offer
    url(r'^offer/$' , views.OfferListApiView.as_view()),
    url(r'^offer/(?P<id>[\w-]+)/$' , views.OfferDetailApiView.as_view() , name = 'detail'),
    url(r'^offer/(?P<id>[\w-]+)/delete/$' , views.OfferDeleteApiView.as_view() , name = 'delete'),
    url(r'createoffer/' , views.OfferCreateApiView.as_view() , name = 'create'),
    #Car
    url(r'^car/$' , views.CarListApiView.as_view()),
    url(r'^car/(?P<license>[\w-]+)/$' , views.CarDetailApiView.as_view() , name = 'detail'),
    url(r'^car/(?P<license>[\w-]+)/delete/$' , views.CarDeleteApiView.as_view() , name = 'delete'),
    url(r'createcar/' , views.CarCreateApiView.as_view() , name = 'create'),
    #City
    url(r'^city/$' , views.CityListApiView.as_view()),
    url(r'^city/(?P<city_name>[\w-]+)/$' , views.CityDetailApiView.as_view() , name = 'detail'),
    url(r'^city/(?P<city_name>[\w-]+)/delete/$' , views.CityDeleteApiView.as_view() , name = 'delete'),
    url(r'createcity/' , views.CityCreateApiView.as_view() , name = 'create'),

    url('get_location/', views.get_location),
    url('get_location_2/', views.get_location_2),
    #Vote
]
