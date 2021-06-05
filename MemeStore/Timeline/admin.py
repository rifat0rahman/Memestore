from django.contrib import admin
from Timeline.models import Post,Postfiles,Follow,Stream,Tag,Likes
# Register your models here.
admin.site.register(Post)
admin.site.register(Postfiles)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Tag)
admin.site.register(Likes)

