from rest_framework import serializers

from .models import Posting, UserPostRelation, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'
        ordering = ['-id']


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    saves_count = serializers.SerializerMethodField(read_only=True)

    post_image = PostImageSerializer(allow_null=True, required=False, many=True)

    def get_likes_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, like=True).count()

    def get_saves_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, saved=True).count()

    class Meta:
        model = Posting
        fields = ('id', 'title', 'user', 'content', 'created_at', 'updated_at', 'paid_content', 'who_liked',
                  'likes_count', 'saves_count', 'post_image', 'categories')
        read_only_fields = ('who_liked', )
        write_only_fields = ('paid_content', )
        ordering = ['-id']


class UserPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = "__all__"
        ordering = ['-id']
