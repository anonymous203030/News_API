from rest_framework import serializers

from .models import Subscription, SubscriptionRelation


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        ordering = ['-id']


class SubscriptionRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRelation
        fields = '__all__'
        ordering = ['-id']