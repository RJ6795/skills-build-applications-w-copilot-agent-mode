from django.urls import path, include


# REST api endpoint format https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
# example full url: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/

urlpatterns = [
    path('', include('octofit_tracker.urls')),
]
