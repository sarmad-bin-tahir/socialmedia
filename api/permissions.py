from django.contrib.auth.models import Group
from rest_framework import permissions

from post.models import Post


def is_delete_update_allowed(request, post_id):
    try:
        post = Post.objects.filter(pk=post_id, user_id=request.user).exists()
        if post:
            return True
        else:
            return False
    except Group.DoesNotExist:
        return None


class CanUpdateDeletePosts(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "UPDATE" or request.method == "DELETE":
            post_id = request.parser_context.get('kwargs').get('pk', '')
            return is_delete_update_allowed(request, post_id)
        else:
            return True
