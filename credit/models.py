from datetime import datetime
from django.db import models

# Create your models here.

class Credit(models.Model):

    def __repr__(self):

        return "Credit('%s', %d)" % (self.amount, self.interest) 

    amount = models.FloatField(default=0.00)
    interest = models.FloatField(max_length=2)
    term = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

class Report(models.Model):

    amount = models.FloatField(default=0.00)
    amount_average = models.FloatField(default=0.00)
    interest_average = models.FloatField(max_length=2)
    date = models.DateField(default=datetime.now().date())