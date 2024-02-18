from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tracker.models import Activity
from tracker.paginators import ActivityPagination

from tracker.serializers import ActivitySerializer


class ActivityCreateAPIview(generics.CreateAPIView):
    """Создаем новую привычку"""
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]


class ActivityListAPIview(generics.ListAPIView):
    """Список всех привычек, доступно для всех пользователей"""
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    pagination_class = ActivityPagination

    def get_queryset(self):
        return Activity.objects.filter(public=True)


class ActivityRetrieveAPIview(generics.RetrieveAPIView):
    """Смотрим, получаем одну привычку"""
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = ActivityPagination


class ActivityUpdateAPIview(generics.UpdateAPIView):
    """Меняем привычку"""
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = [IsAuthenticated]


class ActivityDestroyAPIview(generics.DestroyAPIView):
    """Удаляем привычку"""
    queryset = Activity.objects.all()
    permission_classes = [IsAuthenticated]


class UserActivityListAPIView(generics.ListAPIView):
    """Список привычек текущего пользователя"""
    serializer_class = ActivitySerializer
    pagination_class = ActivityPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Activity.objects.filter(user=user)