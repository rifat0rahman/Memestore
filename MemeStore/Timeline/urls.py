from django.urls import path
from . import views

urlpatterns = [
    path('timeline/',views.home,name="home"),
    path('videos/',views.videos,name="videos"),
    path('post/',views.post,name="post"),
    path('detailsofposts/<post_id>',views.postdetails,name="postdetails"),
    path('like/',views.likes,name="likes"),
    path('search/',views.search,name="search"),
    path('delete/',views.del_post,name="del_post"),


]
