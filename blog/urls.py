from django.urls import path, include

from .views import PostCreate, MainListView, PostView


urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('create/', PostCreate.as_view(), name='create'),
    path('post/<int:pk>/', PostView.as_view(), name='read'),
]
