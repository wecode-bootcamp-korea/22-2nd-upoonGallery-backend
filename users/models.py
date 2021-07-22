from django.db import models

from core.models import SoftDeleteModel, TimeStampModel

class User(TimeStampModel, SoftDeleteModel):
    kakao_id      = models.CharField(max_length=20, unique=True)
    email         = models.EmailField(max_length=30, unique=True)
    password      = models.CharField(max_length=200, null=True)
    nick_name     = models.CharField(max_length=20)
    birthday      = models.CharField(max_length=20)
    gender        = models.CharField(max_length=10)
    address       = models.CharField(max_length=30, null=True)
    reviewed_arts = models.ManyToManyField('arts.Art', through='reviews.Review', related_name='reviewed_users')

    class Meta:
        db_table = 'users'
