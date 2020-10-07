from django.urls import path

from .feeds import LatestEntriesFeed
from .views import *



urlpatterns = [
        #Lists
    # Users List (Not-Authenticated, Authenticated, Upgraded)
    path(f'any/list/', AnyPostListView.as_view()),
    path(f'logged/list/', LoggedPostListView.as_view()),
    path(f'upgraded/list/', UpgradedPostListView.as_view()),
    #Images
    path(f'image/create/', PostImageCreateViewSet.as_view()),
    path(f'image/list/', PostImageListViewSet.as_view()),
    path(f'image/detail/<int:pk>/', PostImageDetailViewSet),
    #Detail And Create
    path(f'detail/<int:pk>/', PostDetail.as_view()),
    path(f'create/', PostCreate.as_view()),
    path(f'custom/list/', CustomPostViewSet.as_view()),
        #User Post Relation (Likes, Saves)
    path(f'relation/create/', UserPostRelationCreate.as_view()),
    path(f'relation/list/', UserPostRelationList.as_view()),
    path(f'relation/detail/<int:pk>/', UserPostRelationDetail.as_view()),
        #Custom User Post Relation
    path(f'custom/relation/list/', CustomUserPostRelationListViewSet.as_view()),
    #
    path(f'upgraded/subscription/list/', UpgradedSubscriptionPostsList.as_view()),
    path(f'logged/subscription/list/', LoggedSubscriptionPostsList.as_view()),
    path(f'latest/feed/', LatestEntriesFeed(), name='news-item'),


]
