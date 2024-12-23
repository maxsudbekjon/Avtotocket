# from django.shortcuts import render
# from drf_spectacular.utils import extend_schema
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
#
# from management.models import Route, Seat, Admin
# from management.serializer import RouteModelSerializer, SeatModelSerializer, AdminModelSerializer
#
#
# # Create your views here.
# @extend_schema(tags=['route'])
# class RouteListAPIView(ListAPIView):
#     queryset = Route.objects.all()
#     serializer_class = RouteModelSerializer
#
# @extend_schema(tags=['route'])
# class RouteCreateAPIView(CreateAPIView):
#     queryset = Route.objects.all()
#     serializer_class = RouteModelSerializer
#
# @extend_schema(tags=['route'])
# class RouteUpdateAPIView(UpdateAPIView):
#     queryset = Route.objects.all()
#     serializer_class = RouteModelSerializer
#     lookup_field = 'id'
#
# @extend_schema(tags=['route'])
# class RouteDeleteAPIView(DestroyAPIView):
#     queryset = Route.objects.all()
#     lookup_field = 'id'
#
#
# # ---------  SEAT   --------------------
#
#
#
# @extend_schema(tags=['seat'])
# class SeatListAPIView(ListAPIView):
#     queryset = Seat.objects.all()
#     serializer_class = SeatModelSerializer
#
#
# @extend_schema(tags=['seat'])
# class SeatCreateAPIView(CreateAPIView):
#     queryset = Seat.objects.all()
#     serializer_class = SeatModelSerializer
#
#
# @extend_schema(tags=['seat'])
# class SeatTicketUpdateAPIView(UpdateAPIView):
#     queryset = Seat.objects.all()
#     serializer_class = SeatModelSerializer
#     lookup_field = 'id'
#
#
# @extend_schema(tags=['seat'])
# class SeatDeleteAPIView(DestroyAPIView):
#     queryset = Seat.objects.all()
#     lookup_field = 'id'
#
#
# # --------   ADMIN   ---------------
#
#
# @extend_schema(tags=['admin'])
# class AdminListAPIView(ListAPIView):
#     queryset = Admin.objects.all()
#     serializer_class = AdminModelSerializer
#
#
# @extend_schema(tags=['admin'])
# class AdminCreateAPIView(CreateAPIView):
#     queryset = Admin.objects.all()
#     serializer_class = AdminModelSerializer
#
#
# @extend_schema(tags=['admin'])
# class AdminTicketUpdateAPIView(UpdateAPIView):
#     queryset = Admin.objects.all()
#     serializer_class = AdminModelSerializer
#     lookup_field = 'id'
#
#
# @extend_schema(tags=['admin'])
# class AdminDeleteAPIView(DestroyAPIView):
#     queryset = Admin.objects.all()
#     lookup_field = 'id'
