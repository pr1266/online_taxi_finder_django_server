from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name']

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(City)
admin.site.register(Location)
admin.site.register(Passenger)
admin.site.register(Driver)
admin.site.register(Offer)
admin.site.register(Car)
admin.site.register(Travel)
admin.site.register(Common)
admin.site.register(Passenger_vote)
admin.site.register(Driver_vote)
admin.site.register(Pre_Vote)
admin.site.unregister(Group)

