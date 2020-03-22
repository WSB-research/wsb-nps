from django.db import models


class Company(models.Model):
    series_lei = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    series_name = models.CharField(max_length=256)
    rep_pd_date = models.DateField()
    total_assets = models.FloatField()
    total_liabilities = models.FloatField()
    net_assets = models.FloatField()
