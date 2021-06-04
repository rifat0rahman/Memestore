from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from Timeline.models import Post
from Authentication.models import Profile
from Timeline.models import Follow,Stream,Post
from django.contrib.auth.models import User
from Authentication.forms import ProfileForm
from django.shortcuts import get_object_or_404
from django.db import transaction
from allauth.account.views import LoginView, SignupView ,PasswordChangeView,PasswordSetView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from chat.models import Directors
from django.db.models import Q
# Create your views here.
@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        current_user = request.user
        ### creating the chat message url
        chat_url1 = str(user) + str(current_user)
        chat_url2 = str(current_user) + str(user)
        # chat url
        chat_url = chat_url1
        # check the user and the current user is not the same
        if user != current_user:
            #check wether a directors is created
            is_created = Directors.objects.filter(Q(directors=chat_url1) | Q(directors=chat_url2))
            #if yes create one,if not grab that
            if not is_created:
                chat_url,created = Directors.objects.get_or_create(directors=chat_url,creator1=current_user,creator2=user)
            else:
                chat_url = is_created[0]
            #### ends chat

        if user:
            # post
            posts = Post.objects.filter(user=user)
            profile = Profile.objects.get(user=user)
            
            # follow 
            is_follow = Follow.objects.filter(follower=request.user,following=user).exists()
            my_followers = Follow.objects.filter(following=user)
            me_followings = Follow.objects.filter(follower=user)

            # context
            context = {
                'posts':posts,
                'profile':profile,
                'my_followers':my_followers,
                'me_following':me_followings,
                'is_follow':is_follow,
                'chat_url':chat_url,
            }
            return render(request,'profile/profile.html',context)
    except:
        return render(request,"error.html")

@login_required
def editprofile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            name = form.cleaned_data.get('name')
            bio = form.cleaned_data.get('bio')

            profile.name = name
            profile.bio  = bio
            if picture:
                profile.picture = picture
                profile.save()
            profile.save()

    else:
        values = {
            'name': profile.name,
            'bio':profile.bio
        }
        form = ProfileForm(initial=values)

    context={
        "profile":profile,
        'form':form,
    }
    
    return render(request,'profile/editprofile.html',context)

@login_required
def follow(request,username,option):
    user = request.user
    following =User.objects.get(username = username)
    try:
        follow,created = Follow.objects.get_or_create(following=following,follower=user)

        if option =='unfollow':
            follow.delete()
            Stream.objects.filter(followed=following,user=user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:15]
            
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post,user=user,followed=following,post_date=post.post_time)
                    stream.save()
        
        return HttpResponseRedirect(reverse('profile',args=[username]))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile',args=[username]))

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("changepassword")
    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.has_usable_password():
            return HttpResponseRedirect(reverse("set_password"))
        return super(PasswordChangeView, self).render_to_response(
            context, **response_kwargs
        )


class CustomPasswordSetView(PasswordSetView):
    success_url = reverse_lazy("changepassword")
    def messages(self):
        return messages.success(self.request, 'Profile details updated.')

def secureaccount(request):
    return render(request,'profile/secureaccount.html')

def managenotification(request):
    return render(request,'profile/managenotification.html')

def contactus(request):
    return render(request,'profile/contactus.html')

def privacy(request):
    return render(request,'profile/privacy.html')