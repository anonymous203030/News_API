from rest_framework import filters

# from .models import User
from posts.models import Posting


class IsOwnerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)

class NotAuthenticated(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user == None:
            return queryset.filter(paid_content=False)

class NotUpgraded(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_upgraded == False:
            return Posting.objects.filter(paid_content=False)

class UserUpgraded(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_upgraded == True:
            return Posting.objects.all()