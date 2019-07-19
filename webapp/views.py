from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializer import EmployessSerializer

# Create your views here.
class EmployeesList(APIView):
    def get(self, request):
        employess1 = Employees.objects.all()
        serializer = EmployessSerializer(employess1, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass
