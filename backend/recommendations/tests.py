import unittest
from django.urls import reverse
from django.test import Client
from .models import Recommendation
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_recommendation(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["author"] = "author"
    defaults["amazon"] = "amazon"
    defaults.update(**kwargs)
    return Recommendation.objects.create(**defaults)


class ByCountTest(unittest.TestCase):
    '''
    Tests for Book Recommendations
    '''
    def setUp(self):
        self.client = Client()

    def test_count_recommendation(self):
        url = reverse('by_count')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
