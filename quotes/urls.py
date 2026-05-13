from django.urls import path
from . import views


urlpatterns = [
    path('/new', views.NewQuoteView.as_view() , name='add_quote'),
    path('/edit/<pk>', views.EditQuoteView.as_view() , name='edit_quote'),
]