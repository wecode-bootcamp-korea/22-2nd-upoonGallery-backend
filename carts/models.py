from django.db import models

from core.models import TimeStampModel

class Cart(TimeStampModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    art  = models.ForeignKey('arts.Art', on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = 'carts'