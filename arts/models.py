from django.db import models

from core.models import SoftDeleteModel, TimeStampModel

class Art(TimeStampModel, SoftDeleteModel):
    title        = models.CharField(max_length=30)
    image_url    = models.URLField()
    description  = models.TextField()
    price        = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    artist       = models.ForeignKey('Artist', on_delete=models.CASCADE)
    size         = models.ForeignKey('Size', on_delete=models.CASCADE)
    shape        = models.ForeignKey('Shape', on_delete=models.CASCADE)
    themes       = models.ManyToManyField('Theme', through='ArtTheme', related_name='arts')
    colors       = models.ManyToManyField('Color', through='ArtColor', related_name='arts')

    class Meta:
        db_table = 'arts'

class Artist(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'artists'

class Size(models.Model):
    name = models.IntegerField()

    class Meta:
        db_table = 'sizes'

class Shape(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'shapes'

class Theme(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'themes'

class Color(models.Model):
    name = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'colors'

class ArtTheme(models.Model):
    art   = models.ForeignKey('Art', on_delete=models.CASCADE)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    class Meta:
        db_table = 'arts_themes'

class ArtColor(models.Model):
    art   = models.ForeignKey('Art', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)

    class Meta:
        db_table = 'arts_colors'