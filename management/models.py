# from django.db.models import Model, CharField, DecimalField, DateTimeField, BooleanField, \
#     ForeignKey, CASCADE, IntegerField
# from phonenumber_field.modelfields import PhoneNumberField
#
# # Create your models here.
#
# class Admin(Model):
#     username = CharField(max_length=255)
#     first_name = CharField(max_length=255)
#     last_name = CharField(max_length=255)
#     email = CharField(max_length=255)
#     password = CharField(max_length=255)
#     role = CharField(max_length=50, choices=[('super_admin', 'Super_Admin'),('admin', 'Admin'), ('practitioner', 'Practitioner'), ('driver', 'Driver'), ('moderator', 'Moderator'), ('operator', 'Operator')   ])
#     created_at = DateTimeField(auto_now_add=True)
#     phone_number=PhoneNumberField(region='UZ')
#
# class Transport(Model):
#     type = CharField(max_length=255, choices=[('bus', 'Bus'), ('train', 'Train'),('plane','Plane')])
#     name = CharField(max_length=255)
#     capacity = IntegerField()
#     created_at = DateTimeField(auto_now_add=True)
#
# class Route(Model):
#     transport = ForeignKey('Transport', on_delete=CASCADE)
#     start_location = CharField(max_length=255)
#     end_location = CharField(max_length=255)
#     departure_time = DateTimeField()
#     arrival_time = DateTimeField()
#     price = DecimalField(max_digits=10, decimal_places=2)
#     driver_id =IntegerField()
#     station_id = ForeignKey('Station', on_delete=CASCADE)
#
# class Seat(Model):
#     route = ForeignKey(Route, on_delete=CASCADE)
#     seat_number = IntegerField()
#     is_available = BooleanField(default=True)
#
# class Station(Model):
#     name = CharField(max_length=255)
#     location = CharField(max_length=255)
#     type = CharField(max_length=50,choices=[('bus_station', 'Bus_station'), ('train_station', 'Train_station')])
#     region = ForeignKey('apps.Region', on_delete=CASCADE)
#
# class RouteStation(Model):
#     route = ForeignKey('Route', on_delete=CASCADE)
#     station = ForeignKey('Station', on_delete=CASCADE)
#     arrival_time = DateTimeField()
#     departure_time = DateTimeField()
