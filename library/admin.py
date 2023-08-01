from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(bookShelf)
admin.site.register(userBook)
admin.site.register(Group)
admin.site.register(NewsArticle)
admin.site.register(Author)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(FriendRequest)
