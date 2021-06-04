from django.shortcuts import render,redirect
from Comment.models import Comments
from Timeline.models import Post
import json
from django.http import JsonResponse
# Create your views here.

def comment(request):
    user = request.user
    if request.method =="POST":
        data = json.loads(request.body)
        comment = data['comment']
        postid = data['postid']
        post = Post.objects.get(id=postid)
        comments = Comments(user=user,post=post,comment=comment)
        comments.save()

        return JsonResponse({"data":data}, status=201)
    else:
        return redirect('home')
    
    return redirect('home')
