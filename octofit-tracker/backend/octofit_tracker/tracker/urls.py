
from django.urls import path
from .views import (
    UserListCreateView,
    TeamListCreateView,
    ActivityListCreateView,
    WorkoutListCreateView,
    LeaderboardListView,
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users-list-create'),
    path('teams/', TeamListCreateView.as_view(), name='teams-list-create'),
    path('activities/', ActivityListCreateView.as_view(), name='activities-list-create'),
    path('workouts/', WorkoutListCreateView.as_view(), name='workouts-list-create'),
    path('leaderboard/', LeaderboardListView.as_view(), name='leaderboard-list'),
]
