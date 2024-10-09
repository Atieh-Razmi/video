from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video, History_video
from .serializers import VideoSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.models import Subscription

# Create your views here.
class videoView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        srz_data =VideoSerializer(instance=videos, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
    
class VideoCreateView(APIView):
    permission_classes = [IsAdminUser,]
    def post(self, request):
        srz_data = VideoSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VideoUPdateView(APIView):
    permission_classes = [IsAdminUser,]
    def put(self, request, pk):
        video = Video.objects.get(pk=pk)
        srz_data = VideoSerializer(instance=video, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDeleteView(APIView):
    permission_classes = [IsAdminUser,]
    def delete(self, request, pk):
        video = Video.objects.get(pk=pk)
        video.delete() 
        return Response({'maeeage': 'video deleted'}, status=status.HTTP_200_OK)    

class VideoAccessView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, video_id):
        user = request.user
        video = Video.objects.filter(id=video_id).first()
        if not video:
            return Response({'error': 'video not found.'}, status=status.HTTP_404_NOT_FOUND)
        subscription = Subscription.objects.filter(user=user, is_active=True).first()
        if not subscription:
            return Response({'error': 'no active subscription found.'}, status=status.HTTP_403_FORBIDDEN)
        if subscription.subscription_type == Subscription.BASIC and Video.access_level == Video.PERMIUM:
            return Response({'error': 'you need permium subscription.'}, status=status.HTTP_403_FORBIDDEN)
        History_video.objects.create(user=user, video=video)
        return Response({
            'title': video.title,
            'content': video.url
        }, status=status.HTTP_200_OK)

class History_videoView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        user = request.user
        watch_history = History_video.objects.filter(user=user).order_by('watched')
        history_data = []
        for history in watch_history:
            history_data.append({
                'video_title': history.video.title,
                'watched': history.watched
            })
        return Response({
            'user': user.username,
            'watch_history': history_data
        }, status=status.HTTP_200_OK)    
