from django.contrib import admin
from django.utils.safestring import mark_safe

from tms_app.models import Post,  User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'title')
    ordering = ('created', 'id',)
    readonly_fields = ('created',)




class ProfileInline(admin.StackedInline):
    model = Profile
    readonly_fields = ["preview"]



    def preview(self, obj):
        if obj.profile_pic:
            return mark_safe(
                f'<a href="{obj.profile_pic.url}" target="_blank"><img src="{obj.profile_pic.url}" style="max-height: 200px;"></a>')
        else:
            return "No image"

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
