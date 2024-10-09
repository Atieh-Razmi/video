from .models import PaymentHistory
from django.utils import timezone

PaymentHistory.objects.create(
    user= request.user,
    amount=100.00,
    status='successfull'
)
PaymentHistory.objects.create(
    user= request.user,
    amount=100.00,
    status='failed'
)
