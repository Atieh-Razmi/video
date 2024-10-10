from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer, SubscriptionSerializer, commentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Subscription, PaymentHistory, comment
from datetime import timedelta
from django.contrib.auth.models import User
from datetime import datetime
import pytz

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserloginView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        srz_data = UserLoginSerializer(data=request.data)
        if srz_data.is_valid():
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

#views for subscription
class SubscriptionView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        srz_data =SubscriptionSerializer(instance=subscriptions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
    
class SubscriptionCreateView(APIView):
    def post(self, request):
        srz_data = SubscriptionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubscriptionUPdateView(APIView):
    def put(self, request, pk):
        subscriptions = Subscription.objects.get(pk=pk)
        srz_data = SubscriptionSerializer(instance=subscriptions, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
class SubscriptionDeleteView(APIView):
    def delete(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete() 
        return Response({'maeeage': 'video deleted'}, status=status.HTTP_200_OK) 
    

class Re_subscriptionView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error':'user_id not found'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({'error':'user not found'}, status=status.HTTP_404_NOT_FOUND)
        active_subscription = Subscription.objects.filter(user=user, is_active=True).first()  
        if not active_subscription:
            return Response({'error':'no active subscription found'}, status=status.HTTP_404_NOT_FOUND)
        active_subscription.end_date += timedelta(days=30)
        active_subscription.save()
        return Response({'message':'subscription renewed successfully', 'end_date': active_subscription.end_date}, status=status.HTTP_200_OK)

class CancelsubscriptionView(APIView):
    #permission_classes = [IsAuthenticated,]        
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error':'user_id is not found'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({'error':'user not found'}, status=status.HTTP_404_NOT_FOUND)
        active_subscription = Subscription.objects.filter(user=user, is_active=True).first()
        if active_subscription:
            active_subscription.Cancel_subscription()
            return Response({'message':'subscription canceled successfuly'}, status=status.HTTP_200_OK)
        return Response({'error':'no active subscription is found'}, status=status.HTTP_404_NOT_FOUND)
    
class paymenthistoryview(APIView):
    #permission_classes = [IsAuthenticated,]   
    def get(self,request):
        user = request.user
        payments = PaymentHistory.objects.filter(user=user).order_by('-payment_date')
        payment_data = []
        for payment in payments:
            payment_data.append({
                'amount': payment.amount,
                "status": payment.payment_status,
                'payment_date': payment.payment_date
            })
        return Response({
            'user': user.username,
            'payment_history': payment_data
        }, status=status.HTTP_200_OK)   
class RemindinfdaysView(APIView):
    #permission_classes = [IsAuthenticated,]
    def get(self, request):
        user = request.user
        try:
            subscription = Subscription.objects.get(user=user, is_active=True)  
            today = datetime.now(pytz.utc)
            end_date = subscription.end_date.astimezone(pytz.utc)
            reminding_time = end_date - today
            reminding_days = reminding_time.days if reminding_time.days > 0 else 0
            return Response({
                'subscription_type': subscription.subscription_type,
                'reminding_days': reminding_days
            }, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            return Response({
                'error': 'no active subscription found'
            }, status=status.HTTP_404_NOT_FOUND)   

class commentView(APIView):
    def get(self, request):
        comments = comment.objects.all()
        srz_data = commentSerializer(instance=comments, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
    
class commentCreateView(APIView):
    def post(self, request):
        srz_data = commentSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)               
