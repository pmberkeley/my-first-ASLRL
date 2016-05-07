from django.db import models
from django.utils import timezone
import json

class Sign(models.Model):
    English_word = models.CharField(max_length=50)
    hands_used = models.CharField(max_length=30)
    handshape = models.CharField(max_length=30)
    hand_motion = models.CharField(max_length=30)
    hand_movement = models.CharField(max_length=30)
    orientation = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    expression = models.CharField(max_length=30)

    def __unicode__(self):
        return self.English_word

# class Handshapes(models.Model):
#     handshape_name =
#     handshape_categories =
#     handshape_image =
#
#     def __unicode__(self):
#         return self.handshape_name
