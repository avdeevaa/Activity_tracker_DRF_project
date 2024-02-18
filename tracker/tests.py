from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Activity

from django.contrib.auth import get_user_model

User = get_user_model()


class ActivityTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test_user@example.com')
        self.activity_data = {
            "user": self.user,
            'place': 'outside',
            "time": '2024-02-11 11:00',
            'action': "very new activity",
            'is_useful_action': True,
            'activity_time': 15,
            'public': True,
        }
        self.activity = Activity.objects.create(**self.activity_data)

    # def test_create_activity(self):
    #     response = self.client.post("/activity/create/", data=self.activity_data, format='json')
    #     user = User.objects.create(email='test@user.com')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.json(), {
    #         'id': 20,
    #         "user": user,
    #         'place': 'outside',
    #         "time": '2024-02-11 11:00',
    #         'action': "very new activity",
    #         'is_useful_action': True,
    #         'activity_time': 15,
    #         'public': True,
    #     })
    #     self.assertTrue(ActivityTestCase.objects.filter(action="very new activity").exists())

    def test_read_activity(self):
        response = self.client.get("/activities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Activity.objects.filter(action="very new activity").exists())

    def test_update_activity(self):
        updated_data = {
            'place': 'home',
         }
        response = self.client.put(f"/activity/update/{self.activity.id}/", data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.activity.refresh_from_db()
        self.assertEqual(self.activity.place, 'outside')

    def test_destroy_activity(self):
        response = self.client.delete(f"/activity/delete/{self.activity.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        #self.assertFalse(Activity.objects.filter(action='very new activity').exists())
