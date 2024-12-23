# from modeltranslation.translator import translator, TranslationOptions, register
#
# from .admin import AdminModelAdmin
# from .models import Admin, Transport, Route, Seat, Station, RouteStation
#
# @register(Admin)
# class AdminTranslationOptions(TranslationOptions):
#     fields = ('username',
#               'first_name',
#               'last_name',
#               'role',
#               )
#
# @register(Transport)
# class TransportTranslationOptions(TranslationOptions):
#     fields = ('type',
#               'name')
#
# @register(Route)
# class RouteTranslationOptions(TranslationOptions):
#     fields = ('transport',
#               'start_location',
#               'end_location',
#               'station_id')
#
# @register(Seat)
# class SeatTranslationOptions(TranslationOptions):
#     fields = ('route',)
#
# @register(Station)
#
# class StationTranslationOptions(TranslationOptions):
#     fields = ('name',
#               'location',
#               'type',
#               'region')
#
# @register(RouteStation)
#
# class RouteStationTranslationOptions(TranslationOptions):
#     fields = ('route',
#               'station',)
#
#
#
