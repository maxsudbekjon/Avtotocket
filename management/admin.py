# from django.contrib import admin
# from django.contrib.admin import ModelAdmin
#
# from management.models import Admin, Transport, Route, Seat, Station, RouteStation
#
#
# # Register your models here.
# @admin.register(Admin)
# class AdminModelAdmin(ModelAdmin):
#     fields = ['phone_number','password','username','first_name','last_name','email','role']
#     readonly_fields = ['created_at']
#     search_fields = ['username']
# @admin.register(Transport)
#
# class TransportModelAdmin(ModelAdmin):
#     fields = ['type','name','capacity']
#     readonly_fields = ['created_at']
#     search_fields = ['name']
# @admin.register(Route)
#
# class RouteModelAdmin(ModelAdmin):
#     fields = ['start_location','end_location','departure_time','arrival_time','price','driver_id','']
#     readonly_fields = ['transport','station_id']
#     search_fields = ['transport']
#
# @admin.register(Seat)
#
# class SeatModelAdmin(ModelAdmin):
#     fields = ['seat_number','is_available']
#     readonly_fields = ['route']
#     search_fields = ['seat_number']
# @admin.register(Station)
#
# class StationModelAdmin(ModelAdmin):
#     fields = ['name','location','type']
#     readonly_fields = ['region']
#     search_fields = ['seatname_number']
# @admin.register(RouteStation)
#
# class RouteStationModelAdmin(ModelAdmin):
#     fields = ['arrival_time','departure_time']
#     readonly_fields = ['route','station']
#
