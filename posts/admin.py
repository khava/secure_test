from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
