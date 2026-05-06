from django.shortcuts import render
from tools.models import Tool, Technician, ToolCheckout
from tools.serializers import ToolSerializer,TechnicianSerializer, ToolCheckoutSerializer
from rest_framework import viewsets

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer


class ToolCheckoutViewSet(viewsets.ModelViewSet):
    queryset = ToolCheckout.objects.all()
    serializer_class = ToolSerializer


