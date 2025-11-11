from django.db import models

# Create your models here.

from django.utils import timezone

# Basic Activity model to store user activities in MongoDB
class Activity(models.Model):
	user = models.CharField(max_length=150)
	activity_type = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	calories = models.PositiveIntegerField(null=True, blank=True)
	timestamp = models.DateTimeField(default=timezone.now)

	class Meta:
		# Use a sensible collection name in MongoDB
		db_table = 'activities'

	def __str__(self):
		return f"{self.user} - {self.activity_type} ({self.duration_minutes}m)"
