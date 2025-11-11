
from rest_framework import generics
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-joined')
    serializer_class = UserSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all().order_by('-created')
    serializer_class = TeamSerializer

class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer

class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all().order_by('-created')
    serializer_class = WorkoutSerializer

class LeaderboardListView(generics.ListAPIView):
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer
