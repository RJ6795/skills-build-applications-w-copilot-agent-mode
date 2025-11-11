from django.db import models
from django.utils import timezone

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.activity_type} ({self.duration_minutes}m)"
