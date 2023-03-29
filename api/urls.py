from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import FavouriteApiView
from api.views import CommentViewSet

# from api.views import CreateCommentApiView, DeleteCommentApiView


router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet, "comment")

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
    path("", include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("login/", obtain_auth_token, name='api_token_auth'),
    # path("create-comment/", CreateCommentApiView.as_view(), name="create_comment"),
    # path("delete-comment/", DeleteCommentApiView.as_view(), name="delete_comment"),
]
