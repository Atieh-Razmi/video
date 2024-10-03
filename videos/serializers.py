from rest_framework import serializers
from .models import Video, History_video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class HistoryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = History_video
        fields = '__all__'        