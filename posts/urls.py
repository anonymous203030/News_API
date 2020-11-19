from django.urls import path

from .feeds import LatestEntriesFeed
from .views import *


urlpatterns = [
        # Lists
    # Users List (Not-Authenticated, Authenticated, Upgraded)
    path(f'any/list/', AnyPostListView.as_view(), name='any_list'),
    path(f'logged/list/', LoggedPostListView.as_view(), name='logged_list'),
    path(f'upgraded/list/', UpgradedPostListView.as_view(), name='upgraded_list'),

    # Images
    path(f'image/create/', PostImageCreateViewSet.as_view(), name='image_create'),
    path(f'image/list/', PostImageListViewSet.as_view(), name='image_list'),
    path(f'image/detail/<int:pk>/', PostImageDetailViewSet.as_view(), name='image_detail'),

    # Detail And Create
    path(f'detail/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path(f'create/', PostCreate.as_view(), name='post_create'),
    path(f'custom/list/', CustomPostViewSet.as_view(), name='custom_list'),
        # User Post Relation (Likes, Saves)
    path(f'relation/create/', UserPostRelationCreate.as_view(), name='relation_create'),
    path(f'relation/list/', UserPostRelationList.as_view(), name='relation_list'),
    path(f'relation/detail/<int:pk>/', UserPostRelationDetail.as_view(), name='relation_detail'),
        # Custom User Post Relation
    path(f'custom/relation/list/', CustomUserPostRelationListViewSet.as_view(), name='custom_rel_list'),

    # Upgraded
    path(f'upgraded/subscription/list/', UpgradedSubscriptionPostsList.as_view(), name='upgraded_sub_list'),
    path(f'logged/subscription/list/', LoggedSubscriptionPostsList.as_view(), name='logged_sub_list'),
    path(f'latest/feed/', LatestEntriesFeed(), name='news-item'),


]
