from django.shortcuts import render
from rest_framework import permissions, viewsets, status, generics
from django.contrib.auth.models import User
from core.models import Stock, Category, Equipment
from core.serializers import UserSerializer, StockSerializer, CategorySerializer, EquipmentSerializer
from core.permissions import AuthenticatedReadOnlyAndStaffFullAccess


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class StockViewSet(viewsets.ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class EquipmentViewSet(viewsets.ModelViewSet):
#     queryset = Equipment.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# # # functional views
# @api_view(['GET', 'POST'])
# def users_list(request, format=None):
#     """
#     List all users ir create a new user
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         resp = Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             resp = Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             resp = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         resp = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     return resp
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk, format=None):
#     """
#     Retrieve, update, delete
#     """
#     try:
#         user = User.objects.get(pk=pk)
#
#         if request.method == 'GET':
#             serializer = UserSerializer(user)
#             resp = Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = UserSerializer(user, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 resp = Response(serializer.data)
#             else:
#                 resp = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             user.delete()
#             resp = Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             resp = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     except User.DoesNotExist:
#         resp = Response(status=status.HTTP_404_NOT_FOUND)
#
#     return resp
