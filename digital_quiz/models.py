from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    GENDER_C = [
        ("m", "Male"),
        ("f", "Female"),
    ]
    gender = models.CharField(choices=GENDER_C, max_length=1)

    def __str__(self):
        prefix = "M" if self.gender == "m" else "F"
        return f"{prefix}{self.id}"


class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)

    def __str__(self):
        return f"Q{self.id}: {self.text}"


class Response(models.Model):
    participant = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(
        max_length=2, 
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
        ]
    )
    time_taken = models.FloatField(help_text="Time in seconds to answer (max 30s)")

    def __str__(self):
        return f"{self.participant} - Q{self.question.id}: {self.selected_option}"
