# Create your views here.
from rest_framework import generics
from rest_framework import viewsets

from apps.serializer import DiscountSerializer
from apps.serializer import RegionSerializer
from .models import Discount
from .models import Region


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
# # class DiscountCreateView(generics.CreateAPIView):
# #     queryset = Discount.objects.all()
# #     serializer_class = DiscountSerializer
# #
# # # List all regions (GET)
# # class DiscountListView(generics.ListAPIView):
# #     queryset = Discount.objects.all()
# #     serializer_class = DiscountSerializer
# #
# # # Update an existing region (PUT/PATCH)
# # class DiscountUpdateView(generics.UpdateAPIView):
# #     queryset = Discount.objects.all()
# #     serializer_class = DiscountSerializer
# #
# # # Delete a region (DELETE)
# # class DiscountDeleteView(generics.DestroyAPIView):
# #     queryset = Discount.objects.all()
# #     serializer_class = DiscountSerializer
