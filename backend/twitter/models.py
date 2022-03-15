from django.db import models

class Twitt(models.Model):
    """
    Twitt Model
    Defines the attributes of a twitt
    """
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    #TODO improve message
    def __repr__(self):
        return 'new twitt is added by : ' + self.name
