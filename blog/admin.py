from blog.models import Post, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'created']

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'post', 'body', 'created']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
