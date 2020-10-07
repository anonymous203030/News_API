from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import *
from .permissions import IsOwner
from .serializers import *
from .filters import IsOwnerFilter

    #COMMENT VIEWSETS

class CommentCreateViewSet(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )


class CommentListViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination


class CommentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwner, IsAdminUser)


class CustomCommentListViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (IsOwnerFilter, )
    pagination_class = PageNumberPagination

    #USER COMMENT RELATION VIEWSETS

class UserCommentRelationCreateViewSet(generics.CreateAPIView):
    queryset = UserCommentRelation.objects.all()
    serializer_class = UserCommentRelationSerializer
    permission_classes = (IsAuthenticated, )


class UserCommentRelationListViewSet(generics.ListAPIView):
    queryset = UserCommentRelation.objects.all()
    serializer_class = UserCommentRelationSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination


class UserCommentRelationDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCommentRelation.objects.all()
    serializer_class = UserCommentRelationSerializer
    permission_classes = (IsOwner, IsAdminUser)

class CustomUserCommentRelationListViewSet(generics.ListAPIView):
    queryset = UserCommentRelation.objects.all()
    serializer_class = UserCommentRelationSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (IsOwnerFilter, )
