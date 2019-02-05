from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Patient
from . serializers import PatientSerializer

class PatientList(APIView):

    def get(self, request):
        patient1 = Patient.objects.all()
        serializer = PatientSerializer(patient1, many=True)
        return Response(serializer.data)

    #def post(self):
    #    pass
