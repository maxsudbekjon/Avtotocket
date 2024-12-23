# from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, IntegerField, EmailField, ManyToManyField
#
#
# # Create your models here.
#
# class Ticket(Model):
#     route = ForeignKey('management.Route', on_delete=CASCADE)
#     seat_number = CharField(max_length=50)
#     status = CharField(max_length=50, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled'), ('paid', 'Paid')])
#     created_at = DateTimeField(auto_now_add=True)
#     order_id=ManyToManyField('Order')
# class Order(Model):
#     email = EmailField()
#     phone_number = IntegerField()
#     payment_date = DateTimeField()
#     card_number = IntegerField()
#     amount = IntegerField()
#     status = CharField(max_length=50, choices=[('complate', 'Complate'), ('pending', 'Pending')])
