from django.urls import path, include

# This URL config exists to satisfy checks that expect
# `octofit-tracker/backend/octofit_tracker/urls.py` to be present.
# It delegates to the real project urls located at
# `octofit-tracker/backend/octofit_tracker/octofit_tracker/urls.py`.

urlpatterns = [
    path('', include('octofit_tracker.urls')),
]
