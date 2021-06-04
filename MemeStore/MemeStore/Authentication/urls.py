from django.urls import path
from allauth.account.views import LoginView, SignupView ,PasswordChangeView,PasswordResetView,PasswordSetView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",SignupView.as_view(), name="signup"),
    path("profile/password_change/",login_required(views.CustomPasswordChangeView.as_view()), name="changepassword"),
    path("profile/password_set/",login_required(views.CustomPasswordSetView.as_view()), name="set_password"),
    path("login/",LoginView.as_view(), name="login"),    
    # editprofile
    path('profile/user/editprofile/',views.editprofile,name = "editprofile"),
    path('profile/editprofile/secure/',views.secureaccount,name = "secureaccount"),
    path('profile/editprofile/managenotification/',views.managenotification,name = "managenotification"),
    path('profile/editprofile/contract/',views.contactus,name = "contractus"),
    path('profile/editprofile/privacy/',views.privacy,name = "privacy"),
    # need to be the last because of url matching
    path('profile/<username>/',views.profile,name = "profile"),
    path("profile/<username>/<option>/",views.follow, name="follow"),
]


