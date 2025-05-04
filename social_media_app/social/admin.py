from django.contrib import admin
from .models import UserProfile, Post, Notification

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Notification)