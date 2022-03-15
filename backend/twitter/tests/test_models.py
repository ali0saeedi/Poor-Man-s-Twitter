from email import message
from django.test import TestCase
from ..models import Tweet


class TweetTest(TestCase):
    """ Test module for Tweet model """

    def setUp(self):
        Tweet.objects.create(
            name='Ali', message='This is a test message')
        Tweet.objects.create(
            name='John', message='This is a second test message!')

    def test_tweet_ownership(self):
        tweet_ali = Tweet.objects.get(name='Ali')
        tweet_john = Tweet.objects.get(name='John')
        self.assertEqual(
            tweet_ali.get_ownership(), "This tweet blong\'s to : Ali")
        self.assertEqual(
            tweet_john.get_ownership(), "This tweet blong\'s to : John")