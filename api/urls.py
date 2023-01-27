from django.urls import path

from api.views import FavoriteApiView

urlpatterns = [
    path("toggle-favorite/", FavoriteApiView.as_view(), name="toggle_favorite"),
]
