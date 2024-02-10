from django.shortcuts import render
from rest_framework import generics
from tracker.models import Activity
from tracker.paginators import ActivityPagination

from tracker.serializers import ActivitySerializer


class ActivityCreateAPIview(generics.CreateAPIView):
    """Создаем новую привычку"""
    serializer_class = ActivitySerializer
    # permission_classes = [IsAuthenticated]


class ActivityListAPIview(generics.ListAPIView):
    """Список всех привычек"""
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = ActivityPagination


class ActivityRetrieveAPIview(generics.RetrieveAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]
    pagination_class = ActivityPagination


class ActivityUpdateAPIview(generics.UpdateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]


class ActivityDestroyAPIview(generics.DestroyAPIView):
    queryset = Activity.objects.all()
    # permission_classes = [IsAuthenticated]

