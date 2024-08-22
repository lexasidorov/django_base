from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
    path('stock/', views.StockList.as_view(), name='stock-list'),
    path('stock/<int:pk>/', views.StockDetail.as_view(), name='stock-detail'),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('equipment/', views.EquipmentList.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment-detail'),
    path('stock/new', views.stock_list, name='stock-list-new'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
