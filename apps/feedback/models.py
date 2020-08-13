from django.db import models

from ..user.models import User


class Feedback(models.Model):
    controller = models.ForeignKey(User, models.CASCADE, related_name='controller_feedback')
    controller_callsign = models.CharField(max_length=16)
    rating = models.IntegerField()
    pilot_name = models.CharField(max_length=64, null=True, blank=True)
    pilot_email = models.EmailField(null=True, blank=True)
    flight_time = models.DateTimeField(null=True, blank=True)
    flight_callsign = models.CharField(max_length=16, null=True, blank=True)
    comments = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.submitted.strftime("%b %d, %Y @ %H%Mz")} | {self.controller.full_name}'
