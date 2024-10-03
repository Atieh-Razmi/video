from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_time = models.IntegerField()
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title
    
class History_video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    duration_time = models.IntegerField()
    duration_watch = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} watched {self.video.title}'
