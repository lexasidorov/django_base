from django.shortcuts import render
from rest_framework import permissions, viewsets, status, generics
from django.contrib.auth.models import User
from core.models import Stock, Category, Equipment
from core.serializers import UserSerializer, StockSerializer, CategorySerializer, EquipmentSerializer
from core.permissions import AuthenticatedReadOnlyAndStaffFullAccess


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]
