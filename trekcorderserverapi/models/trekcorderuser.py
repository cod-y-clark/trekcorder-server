from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class TrekCorderUser(models.Model):
    '''Model for users to add a username to the Django user model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    