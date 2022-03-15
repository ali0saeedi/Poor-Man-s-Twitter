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

    # insert a new record for a tweet
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'message': request.data.get('message')
        }
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
