from django.urls import path

from api.views import FavouriteApiView, CreateCommentApiView

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
    path("create-comment/", CreateCommentApiView.as_view(), name="create_comment"),
]
