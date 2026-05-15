from rest_framework import routers
from .views import QuoteViewSet
from django.urls import path, include


defaultRouter = routers.DefaultRouter()
defaultRouter.register("" , QuoteViewSet )

urlpatterns = [
    path("/", include(defaultRouter.urls)),
]