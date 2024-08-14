from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('stock/', views.StockList.as_view()),
    path('stock/<int:pk>/', views.StockDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('equipment/', views.EquipmentList.as_view()),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
