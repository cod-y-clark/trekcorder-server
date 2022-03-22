from django.db import models
from trekcorderserverapi.models.trekcorderuser import TrekCorderUser


class Log(models.Model):
    '''Model for users to create logs'''
    title = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(TrekCorderUser,on_delete=models.SET_NULL,null=True,related_name='logs')
    