from django.contrib import admin
from .models import Blog, Replay_Comment, Comment, Category, Likes
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Replay_Comment)
admin.site.register(Category)
admin.site.register(Likes)