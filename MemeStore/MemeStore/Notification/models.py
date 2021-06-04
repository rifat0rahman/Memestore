from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notifications(models.Model):
    notifications_type = ((1,'like'),(2,'comment'),(3,'follow'))

    post = models.ForeignKey("Timeline.Post",on_delete=models.CASCADE,related_name="postnoti",blank=True, null=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sendnoti")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE,related_name="recievenoti")
    text_preview = models.CharField( max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    noti_type = models.IntegerField(choices=notifications_type)