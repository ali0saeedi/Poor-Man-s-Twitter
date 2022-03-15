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

class CreateNewTweetTest(TestCase):
    """ Test module for inserting a new tweet """

    def setUp(self):
        self.valid_payload = {
            'name': 'Jack',
            'message' : 'This a message from Jack.'
        }
        self.invalid_payload = {
            'name': '',
            'message' : 'This is a message from John.'
        }

    def test_create_valid_tweet(self):
        response = client.post(
            reverse('tweets'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_tweet(self):
        response = client.post(
            reverse('tweets'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)