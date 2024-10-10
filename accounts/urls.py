from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter



urlpatterns =[
    path('register/', views.UserRegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscription/', views.SubscriptionView.as_view()),
    path('subscription/create/', views.SubscriptionCreateView.as_view()),
    path('subscription/update/<int:pk>/', views.SubscriptionUPdateView.as_view()),
    path('subscription/delete/<int:pk>/', views.SubscriptionDeleteView.as_view()),
    path('subscription/resubscription/', views.Re_subscriptionView.as_view()),
    path('subscription/cancelsubscription/', views.CancelsubscriptionView.as_view()),
    path('payment_history/', views.paymenthistoryview.as_view()),
    path('subscription/Remindinfdays/', views.RemindinfdaysView.as_view()),
    path('comment/', views.commentView.as_view()),
    path('comment/create/', views.commentCreateView.as_view()),
]
