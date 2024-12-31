from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>{request.tenant} Home Page<h1>")
@api_view(['POST'])
def create_staff(request):
    org = request.tenant
    name = request.data.get('name')
    try:
        staff = Staff.objects.create(name=name)
        return Response({'id': staff.id, 'name': staff.name})
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['GET'])
def get_staff(request):
    org = request.tenant
    try:
        staff = Staff.objects.all()
        response = [
            {
                'organization': str(org),
                'id': s.id,
                'name': s.name
            } 
            for s in staff
        ]
        return Response(response)
    except Exception as e:
        return Response({'error': str(e)})
