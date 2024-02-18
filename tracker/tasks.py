from celery import shared_task

from datetime import timedelta, datetime
from django.utils import timezone

from config import settings
from tracker.models import Activity
from key_names import TG_API, TG_id
import requests


@shared_task
def tg_send_message():
    """Посылает сообщение в телеграм, когда надо выполнить активность.
    по логике вещей это фоновая задача, потому что раз в день она включится и проверит,
    если день соответствует сегодня, то тогда пошлет сообщение..."""
    today = timezone.now()
    print("it works yes yes yes ")
    for obj in Activity.objects.all():
        if obj.time == today:
            print("it works yes yes yes ")
            params = {'chat_id': TG_id,
                      "text": f"Hi, friend, it's time to be active! "
                              f"Do it right now {obj.action},"
                      }
            requests.get(f'https://api.telegram.org/bot{TG_API}/sendMessage', params=params).json()
            if obj.periodicity == 'daily':
                obj.time = today + timedelta(days=1)
                obj.save()
            elif obj.periodicity == 'once a week':
                obj.time = today + timedelta(days=7)
                obj.save()
            else:
                obj.time = today + timedelta(days=3)
                obj.save()


