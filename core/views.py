from rest_framework import generics, status
from django.contrib.auth.models import User
from core.models import Stock, Category, Equipment
from core.System.Serializer.old_serializers import oldUserSerializer, oldStockSerializer, oldCategorySerializer, \
    oldEquipmentSerializer
from core.permissions import AuthenticatedReadOnlyAndStaffFullAccess

from core.System.Serializer.StockSerializer import StockSerializer
from core.System.Entities.StockEntity import StockEntity
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = oldUserSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = oldUserSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = oldStockSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = oldStockSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = oldCategorySerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = oldCategorySerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = oldEquipmentSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = oldEquipmentSerializer
    permission_classes = [AuthenticatedReadOnlyAndStaffFullAccess]


@api_view(['GET', 'POST'])
def stock_list(request):
    if request.method == 'GET':
        stocks = Stock.objects.all()  # получить все объекты из БД
        serializer = StockSerializer  # сериализатор
        data = {'data': []}
        for stock in stocks:
            data['data'].append(serializer.serialize(stock))

        resp = Response(data, status=status.HTTP_200_OK)

    else:
        resp = Response({'status': 'error'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return resp
