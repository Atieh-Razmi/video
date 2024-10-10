from django.contrib import admin
from .models import Subscription, PaymentHistory, comment

# Register your models here.
admin.site.register(Subscription)
admin.site.register(PaymentHistory)
@admin.register(comment)
class commentadmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'created')
    raw_id_fields = ('user', 'video')