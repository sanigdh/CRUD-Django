from rest_framework import serializers
from EmployeeApp.models import Department,Employees


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'DepartmentId',
            'DepartmentName'
        )


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'EmployeeId',
            'EmployeeName',
            'Department',
            'DateOfJoining',
            'PhotoFileName'
        )
