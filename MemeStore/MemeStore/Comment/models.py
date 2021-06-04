from django.db import models
from Timeline.models import Post
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from Notification.models import Notifications
# Create your models here.

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    def comment_noti(sender,instance,*args, **kwargs):
        comment = instance
        post = comment.post
        text = str(comment.user)+ " commented to your meme"
        notify = Notifications(post=post,sender=comment.user,reciever=post.user,noti_type=2,text_preview=text)
        notify.save()

    def del_comment_noti(sender,instance,*args, **kwargs):
        comment = instance
        post = comment.post
        notify = Notifications.objects.filter(post=post,sender=comment.user,reciever=post.user,noti_type=2)
        notify.delete()

    def __str__(self):
        return str(self.id) + str(self.comment_time)
    
#notify comment
post_save.connect(Comments.comment_noti,sender=Comments)
post_delete.connect(Comments.del_comment_noti,sender=Comments)