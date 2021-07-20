from django.db import models

from core.models import TimeStampModel

class Review(TimeStampModel):
    comment = models.TextField()
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    art     = models.ForeignKey('arts.Art', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    image_url = models.URLField()
    review    = models.ForeignKey('Review', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviewimages'