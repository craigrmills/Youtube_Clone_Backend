from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('comments', views.CommentList)

urlpatters = [
    path('', include(router.urls)),
]
