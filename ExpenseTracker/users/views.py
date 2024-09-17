from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import redis
import smtplib, ssl, random

# Create your views here.

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.date.get('password')
        user = get_object_or_404(User, email=email) 
        if user.check_password(password):
            refresh = RefreshToken.for_user(user=user)
            return Response({"refresh":str(refresh), 'access':str(refresh.access_token)},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error':'incorrect password'}, status=status.HTTP_400_BAD_REQUEST)


class signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        pass

class send_otp(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "hosseinabedinipoco@gmail.com"  # Enter your address
        receiver_email = request.data.get('email')  # Enter receiver address
        password = "rauxzpjalhevxjvz"
        num = random.randint(1000, 9999)
        message = str(num)
        r.setex(receiver_email, message, 120)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return Response({'message':'seccusful'}, status=status.HTTP_200_OK)    
