from django.shortcuts import render

from .models import Employee, Equipment
from django.views import generic

# Create your views here.
class DashboardView(generic.ListView):
    model = Equipment
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment_service'] = Equipment.objects.filter(condition='Needs Repair')
        context['nbar'] = 'home'
        return context

class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'employees.html'
    context_object_name = 'employee_dt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'employees'
        return context

class EmployeeDetail(generic.DetailView):
    model=Employee
    template_name = 'employee-detail.html'

class EquipmentList(generic.ListView):
    model = Equipment
    context_object_name = 'equipment_list'
    template_name = 'equipment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'equipment'
        return context

