import datetime
from datetime import date

from django.db.models import Model, CharField, TextChoices, DecimalField, DateField
from django.utils.translation import gettext as _, get_language
from parler.models import TranslatableModel, TranslatedFields


class Region(TranslatableModel):

    translations = TranslatedFields(
        name = CharField(_("Name"), max_length=200)
    )
    def __unicode__(self):
        return self.name



class Discount(TranslatableModel):
    class DISCOUNT_TYPE(TextChoices):
        FIXED='fixed',_('Fixed')
        PERCENT='percent',_('Percent')

    translations = TranslatedFields(
        code=CharField(_("Code"), max_length=255),


    )
    discount_value = DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    valid_from = DateField(_("Valid From"))
    valid_to = DateField(_("Valid To"))
    discount_type = CharField(_("Discount_type"),max_length=50, choices=DISCOUNT_TYPE.choices,default=DISCOUNT_TYPE.FIXED)

#
#
#
#
#
# class Notification(Model):
#     user_id =IntegerField()
#     message = TextField()
#     created_at = DateTimeField(auto_now_add=True)
#     is_read = BooleanField(default=False)
#
#
# class Review(Model):
#     driver_id = IntegerField()
#     rating = IntegerField()
#     comment = TextField()
#     created_at = DateTimeField(auto_now_add=True)
#     order = ForeignKey('payment.Order', on_delete=CASCADE)
