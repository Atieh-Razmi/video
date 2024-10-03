from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework import status

# Create your views here.
class videoView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        srz_data =VideoSerializer(instance=videos, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)