from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet

router = DefaultRouter()
router.register(r'regions', RegionViewSet, basename='region')
# router = DefaultRouter()
# router.register(r'discount', DiscountViewSet, basename='discount')
urlpatterns = [
    path('', include(router.urls)),]
# urlpatterns = [
#     path('regions/', RegionListView.as_view(), name='region-list'),
#     path('regions/create/', RegionCreateView.as_view(), name='region-create'),  # POST: Create region
#     path('regions/<int:pk>/update/', RegionUpdateView.as_view(), name='region-update'),
#     path('regions/<int:pk>/delete/', RegionDeleteView.as_view(), name='region-delete'),
#
#     path('discount/', DiscountListView.as_view(), name='discount-list'),
#     path('discount/create/', DiscountCreateView.as_view(), name='discount-create'),  # POST: Create region
#     path('discount/<int:pk>/update/', DiscountUpdateView.as_view(), name='discount-update'),
#     path('discount/<int:pk>/delete/', DiscountDeleteView.as_view(), name='discount-delete'),
# ]
