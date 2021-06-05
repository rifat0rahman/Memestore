from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Timeline.models import Post,Stream,Tag,Postfiles,Likes
from Authentication.models import Profile
from Timeline.forms import PostForm
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.db.models import Q
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
import os
# Create your views here.

@login_required
def home(request):
    user = User.objects.get(username=request.user)

    # collecting the followers postsa and the current users posts
    following_post = Stream.objects.filter(user=user)
    my_post = Post.objects.filter(user=user)
    post_ids = []

    ## collecting posts ids
    # this is from the user's follower
    for post in following_post:
        for content in post.post.content.all():
            if content.file.name.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
                if post.id not in post_ids:
                    post_ids.append(post.post_id)
    #this is itselt user's posts ids
    for post in my_post:
        for content in post.content.all():
            if content.file.name.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
                if post.id not in post_ids:
                    post_ids.append(post.id)
    #collecting the posts  with the id
    posts = Post.objects.filter(id__in=post_ids).order_by('-post_time')
    items = Post.objects.filter(id__in=post_ids).order_by('-post_time').values()

    context = {
        'posts':posts,
        'items':list(items),
        'user':user
    }

    return render(request,'timeline/timeline.html',context)

@login_required
def postdetails(request,post_id):
    try:
        posts = Post.objects.filter(id=post_id)
        post = Post.objects.get(id=post_id)
        
        user_likes = Likes.objects.filter(post=post,user=request.user)
        
        context={
            'posts':posts,
            'user_likes':user_likes,
        }
        return render(request,'timeline/postdetails.html',context)
    except:
        return render(request,'error.html')

@login_required
def post(request):
    user = request.user
    captions = ''
    tags = []
    file_content = []
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('content')
            caption = form.cleaned_data.get('caption')
        
        # get all the tags from caption.
        if caption:
            words = caption.split()
            for word in words:
                if word[0] == '#':
                    is_tag = Tag.objects.filter(tag=word)
                    if is_tag:
                        for tag in is_tag:
                            tags.append(tag)
                    else:
                        tag = Tag(tag=word)
                        tag.save()
                        tags.append(tag)
                else:
                    captions = captions +' '+ word

        for file in files:
            f_instance = Postfiles(file=file,user=user)
            f_instance.save()
            file_content.append(f_instance)
        
        post,created = Post.objects.get_or_create(caption=captions,user=user,post_time=datetime.datetime.now())
        post.content.set(file_content)
        post.tags.set(tags)
        post.save()

        return redirect('home')
    else:
        form = PostForm()

    context = {
        'form':form,
    }
    return render(request,'timeline/post.html',context)

@login_required
def videos(request):
    user = request.user
    # collecting the followers postsa and the current users posts
    following_post = Stream.objects.filter(user=user)
    my_post = Post.objects.filter(user=user)
    videos_ids = []
    
    ## collecting videos and posts ids
    # this is from the user's follower
    for post in following_post:
        for content in post.post.content.all():
            if not content.file.name.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
                if post.id not in videos_ids:
                    videos_ids.append(post.post_id)
    #this is itselt user's posts ids
    for post in my_post:
        for content in post.content.all():
            if not content.file.name.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
                if post.id not in videos_ids:
                    videos_ids.append(post.id)

    #collecting  videos with the id
    videos = Post.objects.filter(id__in=videos_ids).order_by('-post_time')


    context = {
        'videos':videos,
    }
    

    return render(request,'timeline/videos.html',context)

def likes(request):
    # there is no chance of not having a post method here,you can use method==post though
    user = request.user

    count_likes = 0
    current_likes = 0
    
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            postid = data['postid']
        except:
            postid =request.POST.get('post_id')


        post = Post.objects.get(id=postid)
        current_likes = post.likes
        UserLiked = Likes.objects.filter(user=user,post=post).count()

        count_likes = count_likes

        if not UserLiked:
            like = Likes.objects.create(user=user,post=post)
            post_like = Likes.objects.filter(post=post)
            for like in post_like:
                post.liked.add(like)
            current_likes = current_likes + 1
        else:
            unlike = Likes.objects.get(user=user,post=post)
            post.liked.remove(unlike)
            Likes.objects.filter(user=user,post=post).delete()
            current_likes = current_likes - 1
            if current_likes < 0:
                current_likes = 0

        post.likes = current_likes
        post.save()

        return JsonResponse({"likes":current_likes,"isliked":UserLiked}, status=201)


#search
def search(request):
    user = request.user
    if request.method =="GET":
        keywords = request.GET.get('search')
        print(keywords)
        if keywords:
            users = User.objects.filter(username__icontains=keywords)
            return render(request,'timeline/search.html',{'users':users})

    return redirect('home')

#delete post
def del_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        postid = data['postid']
        try:
            Post.objects.get(id=postid).delete()
        except:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

        