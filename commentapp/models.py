from django.db import models

class commentdata(models.Model):
    comment=models.CharField(max_length =100)
