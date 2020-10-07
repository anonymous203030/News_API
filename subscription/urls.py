from django.urls import path

from .views import *

urlpatterns = [
    path('create/', SubscriptionCreateViewSet.as_view()),
    path('list/', SubscriptionListViewSet.as_view()),
    path('detail/<int:pk>/', SubscriptionDetailViewSet.as_view()),
]