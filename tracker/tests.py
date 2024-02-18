from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Activity
from .serializers import ActivitySerializer


class ActivityCreateReadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'user': 1,
            'place': 'home',
            'time': '2024-02-17T12:00:00',
            'action': 'Test action',
            'is_enjoyable_action': False,
            'is_useful_action': True,
            'periodicity': 'daily',
            'reward': 'Test reward',
            'activity_time': 30,
            'public': True
        }
        self.invalid_payload = {
            'action': 'Test action',
            'is_useful_action': True,
            'periodicity': 'dffb',
            'reward': 'Test reward',
        }

    def test_create_valid_activity(self):
        response = self.client.post(
            'http://127.0.0.1:8000/activity/create/',
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_activity(self):
        response = self.client.post(
            'http://127.0.0.1:8000/activity/create/',
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_activity(self):
        response = self.client.get("/activities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_activity(self):
        updated_data = {
                    'place': 'home',
                 }
        response = self.client.put(f"/activity/update/{self.activity.id}/", data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.activity.refresh_from_db()
        self.assertEqual(self.activity.place, 'home')




        # self.client = APIClient()
        # self.activity = Activity.objects.create(
        #         user=1,  # Вставьте существующего пользователя
        #         place='home',
        #         time='2024-02-17T12:00:00',
        #         action='Test action',
        #         is_enjoyable_action=False,
        #         is_useful_action=True,
        #         periodicity='daily',
        #         reward='Test reward',
        #         activity_time=30,
        #         public=True
        #     )

    # def test_read_activity(self):
    #     response = self.client.get("/activities/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue(Activity.objects.filter(action="Test action").exists())



# from django.test import TestCase
#
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from tracker.models import Activity
#
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class ActivityTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(email='test_user@example.com')
#         self.activity_data = {
#             "user": self.user,
#             'place': 'outside',
#             "time": '2024-02-11 11:00',
#             'action': "very new activity",
#             'is_useful_action': True,
#             'activity_time': 15,
#             'public': True,
#         }
#         self.activity = Activity.objects.create(**self.activity_data)
#
#     def test_create_activity(self):
#         response = self.client.post("/activity/create/", data=self.activity_data, format='json')
#         user = User.objects.create(email='test@user.com')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.json(), {
#             'id': 20,
#             "user": user,
#             'place': 'outside',
#             "time": '2024-02-11 11:00',
#             'action': "very new activity",
#             'is_useful_action': True,
#             'activity_time': 15,
#             'public': True,
#         })
#         self.assertTrue(ActivityTestCase.objects.filter(action="very new activity").exists())
#
#     def test_read_activity(self):
#         response = self.client.get("/activities/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue(Activity.objects.filter(action="very new activity").exists())
#
#     def test_update_activity(self):
#         updated_data = {
#             'place': 'home',
#          }
#         response = self.client.put(f"/activity/update/{self.activity.id}/", data=updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.activity.refresh_from_db()
#         self.assertEqual(self.activity.place, 'home')
#
#     def test_destroy_activity(self):
#         response = self.client.delete(f"/activity/delete/{self.activity.id}/")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Activity.objects.filter(action='very new activity').exists())
