from django.db import models

class Tweet(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    #TODO improve message
    def __repr__(self):
        return 'new tweet is added by : ' + self.name

    def get_ownership(self):
        return 'This tweet blong\'s to : ' + self.name
