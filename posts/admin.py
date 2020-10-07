from django.contrib import admin

from .models import Posting, UserPostRelation, PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_at', 'user', 'paid_content',)
    filter_horizontal = ()
    list_filter = ('updated_at', 'created_at', 'paid_content',)
    ordering = ('created_at', )

    search_fields = ('title', 'content', 'user', )


admin.site.register(Posting, PostAdmin)

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'images', )
    filter_horizontal = ()
    list_filter = ('created_at', )
    ordering = ('created_at',)

admin.site.register(PostImage, PostImageAdmin)

class UserPostRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'like', 'saved', 'reacted_at', )
    filter_horizontal = ()
    list_filter = ('saved', 'like', 'reacted_at', )
    ordering = ('reacted_at', )

    search_fields = ('user', 'post', )

admin.site.register(UserPostRelation, UserPostRelationAdmin)
