from django.contrib import admin

from tms_app.models import Post, UserProfile, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'title')
    ordering = ('created', 'id',)
    readonly_fields = ('created',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    ordering = ('id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    ordering = ('id',)
    readonly_fields = ('created',)