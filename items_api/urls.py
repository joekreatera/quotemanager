from rest_framework import routers
from .views import ItemViewSet
from django.urls import path, include


defaultRouter = routers.DefaultRouter()
defaultRouter.register("" , ItemViewSet )

urlpatterns = [
    path("/", include(defaultRouter.urls)),
]