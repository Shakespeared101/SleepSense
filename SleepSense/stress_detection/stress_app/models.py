from django.db import models
from django.contrib.auth.models import User

class UserInputs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heart_rate = models.FloatField()
    body_movements = models.FloatField()
    respiratory_rate = models.FloatField()
    eeg_data = models.FloatField()
    sleeping_hours = models.FloatField()
    blood_oxygen_level = models.FloatField()
    snoring_rate = models.FloatField()
    limb_movement_rate = models.FloatField()
    stress_level = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

class SleepData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    heart_rate = models.IntegerField()
    body_movements = models.IntegerField()
    respiratory_rate = models.IntegerField()
    eeg_data = models.FloatField()
    sleeping_hours = models.FloatField()
    blood_oxygen_level = models.IntegerField()
    snoring_rate = models.IntegerField()
    limb_movement_rate = models.IntegerField()
    stress_level = models.BooleanField()  # 0 for not stressed, 1 for stressed
    
    def __str__(self):
        return f"Sleep Data for {self.user.username} - Stress Level: {'Stressed' if self.stress_level else 'Not Stressed'}"

