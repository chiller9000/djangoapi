from django.shortcuts import render
from rest_framework import viewsets
from .models import Spot
from .serializers import SpotSerializer

# Create your views here.
class SpotView(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer