# from drf_spectacular.utils import extend_schema
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
#
# from management.models import Route
# from management.serializer import RouteModelSerializer
# from payment.models import Ticket, Order
# from payment.serializer import TicketModelSerializer, OrderModelSerializer
#
#
# # Create your views here.
#
# @extend_schema(tags=['ticket'])
# class TicketListAPIView(ListAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketModelSerializer
#
#
# @extend_schema(tags=['ticket'])
# class TicketCreateAPIView(CreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketModelSerializer
#
#
# @extend_schema(tags=['ticket'])
# class TicketUpdateAPIView(UpdateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketModelSerializer
#     lookup_field = 'id'
#
#
# @extend_schema(tags=['ticket'])
# class TicketDeleteAPIView(DestroyAPIView):
#     queryset = Ticket.objects.all()
#     lookup_field = 'id'
#
#
# # -------   ORDER   --------------------
#
# @extend_schema(tags=['order'])
# class OrderListAPIView(ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderModelSerializer
#
#
# @extend_schema(tags=['order'])
# class OrderCreateAPIView(CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderModelSerializer
#
#
# @extend_schema(tags=['order'])
# class OrderUpdateAPIView(UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderModelSerializer
#     lookup_field = 'id'
#
