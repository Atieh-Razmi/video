from django.urls import path
from . import views


urlpatterns = [
    path('videos/', views.videoView.as_view()),
    path('videos/create/', views.VideoCreateView.as_view()),
    path('videos/update/<int:pk>/', views.VideoUPdateView.as_view()),
    path('videos/delete/<int:pk>/', views.VideoDeleteView.as_view()),
    path('video/<int:video_id>/', views.VideoAccessView.as_view()),
    path('watch_history/', views.History_videoView.as_view()),
]