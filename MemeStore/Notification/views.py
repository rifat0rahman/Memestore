from django.shortcuts import render,redirect
from Notification.models import Notifications
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def notification(request):
    user = request.user
    notifications = Notifications.objects.filter(reciever=user).order_by('-date')
    Notifications.objects.filter(reciever=user,is_seen=False).update(is_seen=True)

    context = {
        'notifications':notifications
    }
    return render(request,'notifications/notification.html',context)


def deletenoti(request,notiid):
    user = request.user
    notification = Notifications.objects.filter(reciever=user,id=notiid)
    notification.delete()

    return redirect('notification')

def CountNotifications(request):
    count_notifications = 0
    if request.user.is_authenticated:
        count_notifications = Notifications.objects.filter(reciever=request.user,is_seen=False).count()

    return {'count_notifications':count_notifications}
