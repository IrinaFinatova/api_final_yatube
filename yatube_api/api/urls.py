from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, FollowLightViewSet, GroupViewSet,
                    PostViewSet)

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowLightViewSet, basename='follow')
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [path('v1/', include('djoser.urls')),
               path('v1/', include('djoser.urls.jwt')),
               path('v1/', include(v1_router.urls))]
