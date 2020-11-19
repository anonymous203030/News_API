from django.urls import path

from .views import *

urlpatterns = [
    path('create/', SubscriptionCreateViewSet.as_view(), name='subscription_create'),
    path('list/', SubscriptionListViewSet.as_view(), name='subscription_list'),
    path('detail/<int:pk>/', SubscriptionDetailViewSet.as_view(), name='subscription_detail'),
    path('relation/create/', SubscriptionRelationCreateViewSet.as_view(), name='relation_create'),
    path('relation/list/', SubscriptionRelationListViewSet.as_view(), name='relation_list'),
    path('relation/detail/<int:pk>', SubscriptionRelationDetailViewSet.as_view(), name='relation_detail'),
]