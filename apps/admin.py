from django.contrib import admin
from modeltranslation.translator import register, TranslationOptions
from parler.admin import TranslatableAdmin

from apps.models import Region, Discount


@admin.register(Region)
class RegionAdmin(TranslatableAdmin):
    pass
@admin.register(Discount)
class DiscountAdmin(TranslatableAdmin):
    pass
# @register(Region)
# class RegionTranslationOptions(TranslationOptions):
#     fields = ('name',)
# @admin.register(Notification)
#
# class NotificationModelAdmin(ModelAdmin):
#     fields = ['user_id','message','is_read']
#     readonly_fields = ['created_at']
#     search_fields = ['user_id']
#
# @admin.register(Review)
#
# class ReviewModelAdmin(ModelAdmin):
#     fields = ['driver_id','rating','comment']
#     readonly_fields = ['created_at','order']
#     search_fields = ['driver_id']
