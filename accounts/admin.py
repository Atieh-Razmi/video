from django.contrib import admin
from .models import Subscription, PaymentHistory
# Register your models here.
admin.site.register(Subscription)
admin.site.register(PaymentHistory)