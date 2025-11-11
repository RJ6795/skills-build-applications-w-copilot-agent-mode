from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Activity
from .serializers import ActivitySerializer


class ActivityListCreateView(generics.ListCreateAPIView):
	queryset = Activity.objects.all().order_by('-timestamp')
	serializer_class = ActivitySerializer
