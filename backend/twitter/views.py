from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializer


@api_view(['GET', 'POST'])
def tweets(request):
    # get all tweets
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
        # return Response({})
    # insert a new record for a tweet
    elif request.method == 'POST':
        return Response({})
