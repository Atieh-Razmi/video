from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    BASIC = 'basic'
    PERMIUM = 'premium'
    SUBSCRIPTION_CHOICES = [
        (BASIC, 'Basic'),
        (PERMIUM, 'Premium')
    ]
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES)
    def __str__(self):
        return self.user.username    
    
    def Re_subscription(self, duration):
        self.end_date += duration
        self.is_active = True
        self.save()

    def Cancel_subscription(self):
        self.is_active = False
        self.save()
    
class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    choices ={
        ('S','success'),
        ('F','faild')
    }
    payment_status = models.CharField(max_length=1, choices=choices)
    
    def __str__(self):
        return f'{self.user.username} paid {self.amount} on {self.payment_date}' 

