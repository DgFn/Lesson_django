from django.contrib import admin

from tms_app.models import Post, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'title')
    ordering = ('created', 'id',)
    readonly_fields = ('created',)





@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    ordering = ('id',)
    readonly_fields = ('created',)