from django.db import models

# Create your models here.
class Ads_motorbike(models.Model):

    url = models.TextField()
    title = models.TextField()
    price = models.PositiveIntegerField()
    creation_date = models.DateField()
    views = models.PositiveIntegerField()
    location = models.TextField()
    description = models.TextField()
    seller_type = models.TextField()
    make = models.TextField()
    model = models.TextField()
    engine_displacement = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    kilometers = models.PositiveIntegerField()
    date_scraping = models.DateField()
