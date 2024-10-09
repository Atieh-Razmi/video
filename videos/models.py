from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()
    rate = models.FloatField(default=0)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    BASIC = 'basic'
    PERMIUM = 'premium'
    ACCESS_LEVEL_CHOICES = [
        (BASIC, 'Basic'),
        (PERMIUM, 'Premium')
    ] 
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default=BASIC)
    def __str__(self):
        return self.title
    
class History_video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} watched {self.video.title}'
