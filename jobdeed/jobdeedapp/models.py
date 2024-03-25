from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    USER_TYPE_CHOICES = [
        ('APPLICANT', 'APPLICANT'),
        ('RECRUITER', 'RECRUITER'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)