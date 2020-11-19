from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Subscription, SubscriptionRelation
from .permissions import IsOwner
from .serializers import SubscriptionSerializer, SubscriptionRelationSerializer


# SUBSCRIPTION API VIEWS
class SubscriptionCreateViewSet(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionListViewSet(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsOwner, IsAdminUser, )


# SUBSCRIPTION RELATION API VIEWS
class SubscriptionRelationCreateViewSet(generics.CreateAPIView):
    queryset = SubscriptionRelation.objects.all()
    serializer_class = SubscriptionRelationSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionRelationListViewSet(generics.ListAPIView):
    queryset = SubscriptionRelation.objects.all()
    serializer_class = SubscriptionRelationSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionRelationDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionRelation.objects.all()
    serializer_class = SubscriptionRelationSerializer
    permission_classes = [IsAuthenticated]
