from rest_framework import filters

# from .models import User
from .models import Posting

from subscription.models import SubscriptionRelation


class IsOwnerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)


class UserUpgraded(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.user.is_upgraded == True:
            return Posting.objects.filter()


class LoggedSubscriptionBased(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        subscription = SubscriptionRelation.objects.filter(user=request.user).values('category')
        return Posting.objects.filter(categories__in=subscription).filter(paid_content=False)