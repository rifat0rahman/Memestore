from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.db.models.signals import post_save
from PIL import Image
from Timeline.models import Follow,Post,Stream
from django.db import transaction
# Create your models here.

# user profile here
def user_profile_dir(instance,filename):
    # profile picture path will be here
    profile_picture_name = 'user{0}/profile.jpg'.format(instance.user.id)
    is_axists = os.path.join(settings.MEDIA_ROOT,profile_picture_name)

    if os.path.exists(is_axists):
        os.remove(is_axists)
    return profile_picture_name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=250,null=True,blank=True)
    bio = models.CharField(max_length=150,null=True,blank=True)
    created_time = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to=user_profile_dir,null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

def follow_admin(sender,instance,created,**kwargs):
    if created:
        user = instance
        following = User.objects.get(username="memestore")
        follow = Follow(follower=user,following=following)
        follow.save()
        # push post to user(instance)
        posts = Post.objects.all().filter(user=following)[:15]
        with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post,user=user,followed=following,post_date=post.post_time)
                    stream.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)
post_save.connect(follow_admin,sender=User)


