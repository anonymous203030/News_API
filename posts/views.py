
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import UserPostRelation, Posting, PostImage
from .permissions import *
from .serializers import PostSerializer, UserPostRelationSerializer, PostImageSerializer
from .filters import *
from rest_framework import filters as rest_filters

# Post Create Detail ( Admin User )

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser, )


class PostCreate(CreateAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser, )


class PostImageCreateViewSet(CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAdminUser]


class PostImageListViewSet(ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAdminUser]


class PostImageDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAdminUser]

#   Like,Save ViewSet

class UserPostRelationCreate(CreateAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = (IsAdminUser, IsAuthenticated, )


class UserPostRelationList(ListAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = (IsAdminUser, IsAuthenticated, )
    pagination_class = PageNumberPagination


class UserPostRelationDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = (IsAdminUser, IsOwner, )


#   Posts List View For Non-Logged And Logged But Not Upgraded Users
class AnyPostListView(ListAPIView):
    queryset = Posting.objects.filter(paid_content=False)
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )
    pagination_class = PageNumberPagination
    search_fields = ['title', 'content']


# Posts List View For Logged Users
class LoggedPostListView(ListAPIView):
    queryset = Posting.objects.filter(paid_content=False)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ['title', 'content']


# Posts List View For Upgraded Users
class UpgradedPostListView(ListAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [UserUpgraded]
    search_fields = ['title', 'content']


#   Custom admin posts
class CustomPostViewSet(ListAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner, IsAdminUser]
    pagination_class = PageNumberPagination


# Custom User Likes And Saves
class CustomUserPostRelationListViewSet(ListAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsOwner, IsAdminUser]
    pagination_class = PageNumberPagination


# # User Subscription-Based Posts List
class UpgradedSubscriptionPostsList(ListAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [UserUpgraded]


class LoggedSubscriptionPostsList(ListAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [LoggedSubscriptionBased,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    search_fields = ['categories', 'title', 'content', 'created_at', 'updated_at']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['__all__']
