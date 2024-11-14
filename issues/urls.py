from django.urls import path
from .views import (
    IssueListView,
    IssueDetailView,
    IssueUpdateView,
    IssueDeleteView,
    IssueCreateView
    )

# step 2 mc3 
urlpatterns = [
    path("issues/", IssueListView.as_view(), name="list"),
    path("<int:pk>/", IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", IssueUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", IssueDeleteView.as_view(), name="delete"),
    path("new/", IssueCreateView.as_view(), name="create"),
]