from rest_framework import serializers

from .models import Comment, UserCommentRelation


class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'comment', 'is_liked', 'created_at', 'likes_count', )
        ordering = ['-id']

    def get_likes_count(self, instance):
        return UserCommentRelation.objects.filter(comment=instance, like=True).count()


class UserCommentRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCommentRelation
        fields = ('id', 'user', 'comment', 'like', 'liked_at', )
        ordering = ['-id']
