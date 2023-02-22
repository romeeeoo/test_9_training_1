from django.urls import path, include
from rest_framework import routers

from api.views import FavouriteApiView
from api.views import CommentViewSet

from api.views import CreateCommentApiView, DeleteCommentApiView


router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet, "comment")

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
    path("", include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("create-comment/", CreateCommentApiView.as_view(), name="create_comment"),
    # path("delete-comment/", DeleteCommentApiView.as_view(), name="delete_comment"),
]
