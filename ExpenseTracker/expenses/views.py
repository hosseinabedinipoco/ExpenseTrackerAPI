from django.shortcuts import render
from .models import Expense
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AddExpense(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        expense = ExpenseSerializer(data=request.data, context={'request':request})
        if expense.is_valid():
            expense.save()
            return Response(expense.data, status=status.HTTP_201_CREATED)
        else:
            return Response(expense.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateExpense(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        pass    

class DeleteExpense(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        pass    

class GetExpense(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        pass    