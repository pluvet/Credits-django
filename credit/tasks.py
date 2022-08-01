from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta

from celery import shared_task
from django.http import JsonResponse
from credit.models import Credit, Report

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y

@shared_task
def report():
    
    date = datetime.now().date() - timedelta(days=1)


    credits = Credit.objects.filter(date__gte = date.strftime("%Y-%m-%d") + ' 00:00:00.882454-05') \
                            .filter(date__lte = date.strftime("%Y-%m-%d") + ' 23:59:59.882454-05').values()    
    credits = list(credits)

    typ = str(type(credits))
    #check type 

    max = 0
    average = 0
    rate = 0
    amount=0

    if credits:
        count = 0
        for x in credits:
        
            max = x.get('amount') + max
            rate = x.get('interest') + rate
            count+= 1

        amount = max
        average= max / count
        rate = rate / count

    Report.objects.create(amount=amount, amount_average= average,interest_average= rate)

    datos = { 
        'Credit': 'hola',  
        'message': "Success"
    }
    
    return JsonResponse(datos)
