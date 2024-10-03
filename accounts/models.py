from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_status = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    subscription_startDate = models.DateTimeField(null=True, blank=True)
    ssubscription_endDate = models.DateTimeField(null=True, blank=True)
    #video = models.onetomanyfield or forenkey('Video',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_time = models.IntegerField()

    def __str__(self):
        return self.name    