from django.shortcuts import render
from .models import Expense
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
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
        expense = get_object_or_404(Expense, pk=id)
        if expense.author == request.user:
            serializer = ExpenseSerializer(expense, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'you dont access'}, status=status.HTTP_401_UNAUTHORIZED)    

class DeleteExpense(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        expense = get_object_or_404(Expense, pk=id)
        if expense.author == request.user :
            expense.delete()
            return Response({'messgae':"deleted"}, status=status.HTTP_200_OK)
        else:    
            return Response({'error':'you dont access'}, status=status.HTTP_401_UNAUTHORIZED)


class GetExpense(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        start = request.GET.get('s')
        end = request.GET.get('e')
        expenses = Expense.objects.filter(Q(date__gte=start) & Q(date__lte=end) & Q(author=request.user))
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)