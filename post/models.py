from django.db import models

from api.models import User


class Post(models.Model):
    text = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", default=None)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.text


class PostLikeUnlike(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like_unlike", default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like_unlike", default=None, null=True)
    reaction = models.BooleanField(default=False)


class PostLikeUnlike11(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like_unlike111", default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like_unlike111", default=None, null=True)
    reaction = models.BooleanField(default=False)

