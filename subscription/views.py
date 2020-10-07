from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Subscription
from .permissions import IsOwner
from .serializers import SubscriptionSerializer


class SubscriptionCreateViewSet(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )


class SubscriptionListViewSet(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )


class SubscriptionDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsOwner, IsAdminUser, )


