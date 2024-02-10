from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import ActivityCreateAPIview, ActivityListAPIview, ActivityUpdateAPIview, ActivityRetrieveAPIview, \
    ActivityDestroyAPIview

app_name = TrackerConfig.name


urlpatterns = [
    path('activity/create/', ActivityCreateAPIview.as_view(), name='create_activity'),
    path('activities/', ActivityListAPIview.as_view(), name='all_activities'),
    path('activity/<int:pk>/', ActivityRetrieveAPIview.as_view(), name='get_one_activity'),
    path('activity/update/<int:pk>/', ActivityUpdateAPIview.as_view(), name='update_activity'),
    path('activity/delete/<int:pk>/', ActivityDestroyAPIview.as_view(), name='delete_activity'),
]
