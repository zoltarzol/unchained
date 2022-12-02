from django.db import models

# Create your models here.
class ChatBotInput(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text='Saisis ton prénom')

    input = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        help_text='Pose ta question')
    
    response = models.TextField(
        max_length=10000)

class InputModel(models.Model):
    text_msg = models.TextField(
        max_length = 1000,
        blank= False,
        null = True,
        default= "",
    )