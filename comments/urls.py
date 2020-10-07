from django.urls import path
from .views import *
urlpatterns = [
        #COMMENTS URLS
    path('list/', CommentListViewSet.as_view()),
    path('create/', CommentCreateViewSet.as_view()),
    path('detail/', CommentDetailViewSet.as_view()),
    path('custom/', CustomCommentListViewSet.as_view()),

        #USER COMMENTS RELATION URLS
    path('relation/list/', UserCommentRelationListViewSet.as_view()),
    path('relation/create/', UserCommentRelationCreateViewSet.as_view()),
    path('relation/detail/', UserCommentRelationDetailViewSet.as_view()),
    path('relation/custom/', CustomUserCommentRelationListViewSet.as_view()),
]