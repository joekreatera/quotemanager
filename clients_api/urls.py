from rest_framework import routers
from .views import ClientsViewSet, SpecialClientOps
from django.urls import path, include


defaultRouter = routers.DefaultRouter()
defaultRouter.register("" , ClientsViewSet )

urlpatterns = [
    path("/", include(defaultRouter.urls)),
    path("/special" , SpecialClientOps.as_view() )
]