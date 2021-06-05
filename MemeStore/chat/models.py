from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey(User,related_name = "direct_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name ="direct_seceiver", on_delete=models.CASCADE)
    chat_url = models.ForeignKey("chat.Directors",on_delete=models.CASCADE)
    body =models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    
class Directors(models.Model):
    directors = models.CharField(max_length=100)
    creator1 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creatorone')
    creator2 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creatortwo')
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.directors
        