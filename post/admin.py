from django.contrib import admin
from post.models import Post


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    pass