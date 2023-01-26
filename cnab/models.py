from django.db import models

class CNAB(models.Model):
    transaction_type = models.CharField(max_length=1)
    occurrence_date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    occurrence_hour = models.CharField(max_length=6)
    owner_name = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
