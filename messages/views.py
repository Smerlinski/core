from django.shortcuts import render
from rest_framework import viewsets
from .models import Massage
from .serializers import MessageSerializer

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MessageSerializer
