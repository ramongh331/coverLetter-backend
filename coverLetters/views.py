from django.shortcuts import render
from .models import CoverLetter
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CoverLetterSerializer

# Create your views here.
class CoverLetterViewSet(viewsets.ModelViewSet):
    queryset = CoverLetter.objects.all()
    serializer_class = CoverLetterSerializer
    permission_classes = [permissions.AllowAny]