
from django.db import models

gender = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)
# Create your models here.


class BotUsers (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    sex = models.CharField(max_length=100, choices=gender)

    def __str__(self):
        return self.email
