from django.urls import path
from . import views


urlpatterns = [
    path('/', views.TestClientsView.as_view() , name='test'),
    path('/all', views.ListClientsView.as_view() , name='list'),
    path('/new', views.NewClientView.as_view() , name='add'),
    path('/<pk>', views.DetailClientsView.as_view() , name='detail'),
]