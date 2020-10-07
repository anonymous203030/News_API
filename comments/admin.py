from django.contrib import admin

from .models import Comment, UserCommentRelation


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', )
    list_filter = ('created_at', )
    ordering = ('created_at', )
    search_fields = ('user', 'comment', )

class UserCommentRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'like', )
    list_filter = ('liked_at', )
    ordering = ('liked_at', )
    search_fields = ('user', 'comment', )


admin.site.register(Comment, CommentAdmin)
admin.site.register(UserCommentRelation, UserCommentRelationAdmin)