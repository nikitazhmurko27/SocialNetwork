from django.contrib import admin

from apps.social_network.models import Post


class PostAuthorLikeInline(admin.TabularInline):
    model = Post.likes.through


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
    )
    inlines = [
        PostAuthorLikeInline,
    ]


admin.site.register(Post, PostAdmin)
