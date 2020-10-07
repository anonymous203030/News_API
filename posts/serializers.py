from rest_framework import serializers, fields
from rest_framework.fields import SerializerMethodField

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

    class Meta:
        model = Posting
        fields = ('id', 'title', 'user', 'content', 'created_at', 'updated_at', 'paid_content', 'who_liked', 'likes_count', 'saves_count', 'post_image' )
        read_only_fields = ('who_liked', )
        write_only_fields = ('paid_content', )
        ordering = ['-id']
    #
    # def create(self, validated_data):
    #     images_data = validated_data.pop('images')
    #     post = Posting.objects.create(**validated_data)
    #     for image_data in images_data:
    #         PostImage.objects.create(post=post, **image_data)
    #     return post

    def get_likes_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, like=True).count()

    def get_saves_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, saved=True).count()

class UserPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = "__all__"
        ordering = ['-id']

            #('user', 'post', 'like', 'saved', 'reacted_at',)

