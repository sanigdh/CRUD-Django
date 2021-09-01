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

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializers(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializers(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse(employees_serializer.errors)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializers(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
