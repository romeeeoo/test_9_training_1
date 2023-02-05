from django.urls import path

from api.views import FavouriteApiView

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
]
