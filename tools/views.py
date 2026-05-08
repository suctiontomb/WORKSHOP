from tools.models import Tool, Technician, ToolCheckout
from tools.serializers import ToolSerializer,TechnicianSerializer, ToolCheckoutSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ToolCheckoutViewSet(viewsets.ModelViewSet):
    queryset = ToolCheckout.objects.all()
    serializer_class = ToolSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    


