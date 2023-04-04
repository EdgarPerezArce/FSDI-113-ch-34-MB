from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("posts/new/", PostCreateView.as_view(), name="new"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    
]