from django.shortcuts import render
import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Employee
from .serializers import *

@api_view(['POST'])
def upload_file(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['file']
    df = pd.read_excel(file)

    # Create companies and employees
    companies = {}
    for _, row in df.iterrows():
        company_name = row['company_name']
        if company_name not in companies:
            company, _ = Company.objects.get_or_create(name=company_name)
            companies[company_name] = company

    employees = [
        Employee(
            first_name=row['first_name'],
            last_name=row['last_name'],
            phone_number=row['phone_number'],
            company=companies[row['company_name']]
        )
        for _, row in df.iterrows()
    ]

    Employee.objects.bulk_create(employees)
    
    return Response({'message': 'Data uploaded successfully!'}, status=status.HTTP_201_CREATED)