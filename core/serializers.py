from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Stock, Category, Equipment


class UserSerializer(serializers.ModelSerializer):
    # equipments = serializers.PrimaryKeyRelatedField(many=True, queryset=Equipment.objects.all())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_staff',
            # 'equipments',
        ]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['name', 'address']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class EquipmentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=False)
    stock = StockSerializer(read_only=False)
    user = UserSerializer(read_only=False)
    # category = serializers.HyperlinkedIdentityField(view_name='category-list')
    # stock = serializers.HyperlinkedIdentityField(view_name='category-list')
    # user = serializers.HyperlinkedIdentityField(view_name='category-list')

    class Meta:
        model = Equipment
        fields = ['name', 'category', 'stock', 'user']