from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields = '__all__'
        read_only_fields = ['date', 'author']
    

    def validate_category(self, value):
        if value not in ['Groceries', 'Leisure', 'Electronics', 'Utilities', 'Clothing', 'Health']:
            raise serializers.ValidationError("invalid category")
        return value
    
    def create(self, validated_data):
        request = self.context.get('request')
        expense = Expense.objects.create(
            title = validated_data['title'],
            desc = validated_data['desc'],
            amount = validated_data['amount'],
            author = request.user,
            category = validated_data['category']
        )
        return expense