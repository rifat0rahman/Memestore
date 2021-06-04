from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from chat.models import Chat,Directors
from django.db.models import Q
from django.http import HttpResponse 
# Create your views here.
def chat(request):
    user = request.user
    last_dir = Directors.objects.filter(Q(creator1=user)|Q(creator2=user))
    if last_dir:
        path = last_dir.last().directors
        return redirect('room',path)
    else:
        return render(request,'chatroom/chat.html')

def room(request, room_name):
    user = request.user
    
    #grab the users who talk to the currentuser
    directors = Directors.objects.filter(Q(creator1=user) | Q(creator2=user))

    
    # grab the messages between them
    director = Directors.objects.get(directors=room_name)
    messages =  Chat.objects.filter(chat_url=director)
    #update to seen
    Chat.objects.filter(chat_url=director,is_seen=False).update(is_seen=True)

    context= {
    'room_name': room_name,
    'messages' : messages,
    'directors':directors,
    'current_person':director,

    }

    return render(request, 'chatroom/room.html',context)
        

def countchat(request):
    # to have a number always
    user = request.user
    count_msg = 0
    if user.is_authenticated:
        count_msg = Chat.objects.filter(receiver=user,is_seen=False).count()
    return {'count_msg':count_msg}

    
