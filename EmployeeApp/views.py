from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employees
from EmployeeApp.serializers import DepartmentSerializers,EmployeeSerializers


# Create your views here.


@csrf_exempt

def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializers = DepartmentSerializers(departments,many=True)
        return JsonResponse(departments_serializers.data,safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializers = DepartmentSerializers(data=department_data)
        if departments_serializers.is_valid():
            departments_serializers.save()
            return JsonResponse("Department Added Successfully",safe=False)
        return JsonResponse("Failed to Add Department",safe=True)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializers = DepartmentSerializers(department,data=department_data)
        if departments_serializers.is_valid():
            departments_serializers.save()
            return JsonResponse("Department Updated Successfully",safe=False)
        return JsonResponse("Failed to Update Department",safe=True)
    elif request.method == 'DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Department Deleted Successfully",safe=False)
