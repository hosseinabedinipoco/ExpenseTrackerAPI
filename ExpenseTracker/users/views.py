from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

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
    pass