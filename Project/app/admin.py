from django.contrib import admin
from .models import BlogPost, Category, User, Like, ContactMessage

admin.site.register(User)
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Like)
admin.site.register(ContactMessage)
