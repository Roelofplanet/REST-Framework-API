from django.shortcuts import render
from rest_framework import viewsets
from .models import GovernmentData
from .serializers import GovernmentDataSerializer

class GovernmentDataView(viewsets.ModelViewSet):
    queryset = GovernmentData.objects.all()
    serializer_class = GovernmentDataSerializer
