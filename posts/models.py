from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.TextField(verbose_name='title')
    text = models.TextField(verbose_name='text')
    created_date = models.DateField(auto_now_add=True, verbose_name='created_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='author')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(verbose_name='comment')
    created_date = models.DateField(auto_now_add=True, verbose_name='created_date')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='author')

    def __str__(self):
        return self.comment
    