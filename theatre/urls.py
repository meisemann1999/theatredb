from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('employees/', views.EmployeeList.as_view(), name='employees'),
    path('employees/<pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
    path('equipment/', views.EquipmentList.as_view(), name='equipment')
]