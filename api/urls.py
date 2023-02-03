from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import FavouriteApiView

# router = routers.DefaultRouter()
# router.register(r"")

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
    path("login/", obtain_auth_token, name="api_login"),
]
