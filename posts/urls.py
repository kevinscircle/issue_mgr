from django.urls import path
from .views import (
    PostListView,
    DraftPostListView,
    ArchivedPostListView ,
    DetailPostView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView
    )

# step 2 mc3 
urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", DetailPostView.as_view(), name="post_detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("new/", PostCreateView.as_view(), name="post_create"),
]