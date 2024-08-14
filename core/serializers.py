from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Stock, Category, Equipment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'address']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class EquipmentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=False)
    stock = StockSerializer(read_only=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'category', 'stock', 'user']


    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get_or_create(name=category_data['name'])

        stock_data = validated_data.pop('stock')
        stock = Stock.objects.get_or_create(name=stock_data['name'], defaults={'address': stock_data['address']})

        equipment = Equipment.objects.create(category=category, stock=stock, **validated_data)

        return equipment


    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category = Category.objects.get_or_create(name=category_data['name'])
            instance.category = category

        stock_data = validated_data.pop('stock', None)
        if stock_data:
            stock = Stock.objects.get_or_create(name=stock_data['name'], defaults={'address': stock_data['address']})
            instance.stock = stock

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
