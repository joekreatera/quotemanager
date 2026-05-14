from rest_framework import routers
from .views import ClientsViewSet
from django.urls import path, include


defaultRouter = routers.DefaultRouter()
defaultRouter.register("" , ClientsViewSet )

urlpatterns = [
    path("/", include(defaultRouter.urls))
]