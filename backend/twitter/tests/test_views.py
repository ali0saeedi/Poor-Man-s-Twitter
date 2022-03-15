from email import message
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Tweet
from ..serializers import TweetSerializer


# initialize the APIClient app
client = Client()

class GetAllTweetsTest(TestCase):
    """ Test module for GET all tweets API """

    def setUp(self):
        Tweet.objects.create(
            name='Jack', message="a message from Jack")
        Tweet.objects.create(
            name='Nima', message="a message from Nima")
        Tweet.objects.create(
            name='Ali', message="a message from Ali")
        Tweet.objects.create(
            name='Mina', message="a message from Mina")

    def test_get_all_tweets(self):
        # get API response
        response = client.get(reverse('tweets'))
        # get data from db
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)