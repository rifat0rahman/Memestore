from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from PIL import Image
from Notification.models import Notifications
# Create your models here.
def post_picture_dir(instance,filename):
    picture_path = 'user{0}/posts/{1}'.format(instance.user.id,filename)
    return picture_path

class Tag(models.Model):
    tag = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(null=False,unique=True)
    
    def __str__(self):
        return self.tag

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag[1:])
        return super().save(*args, **kwargs)
    
class Postfiles(models.Model):
    user = models.ForeignKey(User,related_name="postowner", on_delete=models.CASCADE)
    file = models.FileField(upload_to=post_picture_dir)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,related_name="userpost",on_delete=models.CASCADE)
    content = models.ManyToManyField(Postfiles,related_name="content")
    caption = models.TextField(max_length=1500,blank=True,null=True)
    post_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    liked = models.ManyToManyField("Timeline.Likes",blank=True,null=True,related_name='likes')
    tags = models.ManyToManyField(Tag,related_name="tags",blank=True)

    def likes_as_flat_user_id_list(self):
        return self.liked.values_list('user', flat=True)


    def __str__(self):
        display = str (self.user) + str (self.post_time)
        return display

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name="follower")
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="following")

    def follow_noti(sender,instance,*args, **kwargs):
        follow = instance
        follower = follow.follower
        following = follow.following

        text = str(follower)+ ' started following you'
        notify = Notifications(sender=follower,reciever=following,noti_type=3,text_preview=text)
        notify.save()

    def unfollow_noti(sender,instance,*args, **kwargs):
        follow = instance
        follower = follow.follower
        following = follow.following
        notify = Notifications.objects.filter(sender=follower,reciever=following,noti_type=3)
        notify.delete()

    def __str__(self):
        return str(self.following.username)

class Stream(models.Model):
    followed = models.ForeignKey(User,on_delete=models.CASCADE,related_name="stream_followed")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    post_date = models.DateField()

    def create_stream(sender,instance,*args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        
        for follower in followers:
            stream = Stream(followed=user,post=post,post_date=post.post_time,user=follower.follower)
            stream.save()
        
    def __str__(self):
        display = str (self.user) + '--' + str (self.id)
        return display

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userlikes")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="postlikes")

    def like_noti(sender,instance,*args, **kwargs):
        like = instance
        post = like.post
        text = str(like.user)+ ' liked your meme'
        notify = Notifications(post=post,sender=like.user,reciever=post.user,noti_type=1,text_preview=text)
        notify.save()

    def unlike_noti(sender,instance,*args, **kwargs):
        like = instance
        post = like.post
        notify = Notifications.objects.filter(post =post,sender=like.user,reciever=post.user,noti_type=1)
        notify.delete()

    def __str__(self):
        return str(self.user)
    

# stream
post_save.connect(Stream.create_stream,sender=Post)


#notification of follow
post_save.connect(Follow.follow_noti,sender=Follow)
post_delete.connect(Follow.unfollow_noti,sender=Follow)

#notification of follow
post_save.connect(Likes.like_noti,sender=Likes)
post_delete.connect(Likes.unlike_noti,sender=Likes)


