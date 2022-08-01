from datetime import datetime, timedelta
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from credit.tasks import report
from .models import Credit
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .decorators import yesterday
# Create your views here.


# Create your views here.
class CreditView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
            if (id > 0):
                credits = list(Credit.objects.filter(id=id).values())
                if len(credits) > 0:
                    credit = credits[0]
                    datos = {'message': "Success", 'credit': credit}
                else:
                    datos = {'message': "Credit not found..."}
                return JsonResponse(datos)
            else:
                credits = list(Credit.objects.values())
                if len(credits) > 0:
                    datos = {'message': "Success", 'credits': credits}
                else:
                    datos = {'message': "Credits not found..."}
                return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Credit.objects.create(amount=jd['amount'], interest=jd['interest'], term=jd['term'])

        datos = {   
            'Credit': jd,  
            'message': "Success"
        }

        return JsonResponse(datos)

    


    
    class AmountGeneratedView(View):

        @yesterday
        def get(self, request, credits):
            max = 0

            for x in credits:
         
                max = x.get('amount') + max

            return JsonResponse(max, safe=False)
    
    
    class AmountAverageView(View):

        @yesterday
        def get(self, request, credits):

            max = 0         
            count = 0
            for x in credits:
            ## return JsonResponse(x.get('amount') , safe=False)
                max = x.get('amount') + max
                count = count + 1
    
            average = max / count
            return JsonResponse(average, safe=False)

    class InterestAverageView(View):

        @yesterday
        def get(self, request, credits):

            max = 0
            count = 0
            for x in credits:
             ##   return JsonResponse(x.get('interest') , safe=False)
                max = x.get('interest') + max
                count = count + 1
    
            rate = max / count
            return JsonResponse(rate, safe=False)

  
class AmountGeneratedView(View):
    
    def get(self, request):

    
        max = 0
        date = datetime.now().date() - timedelta(days=1)

        credits = Credit.objects.filter(date__gte = date.strftime("%Y-%m-%d") + ' 00:00:00.882454-05') \
                                .filter(date__lte = date.strftime("%Y-%m-%d") + ' 23:59:59.882454-05').values()    
        credits = list(credits)
        
    ##    return JsonResponse(credits, safe=False)

        for x in credits:
           ## return JsonResponse(x.get('amount') , safe=False)
            max = x.get('amount') + max

        return JsonResponse(max, safe=False)

class AmountAverageView(View):
    
    def get(self, request):

        max = 0
        date = datetime.now().date() - timedelta(days=1)


        credits = Credit.objects.filter(date__gte = date.strftime("%Y-%m-%d") + ' 00:00:00.882454-05') \
                                .filter(date__lte = date.strftime("%Y-%m-%d") + ' 23:59:59.882454-05').values()    
        credits = list(credits)
        
    ##    return JsonResponse(credits, safe=False)
        count = 0
        for x in credits:
           ## return JsonResponse(x.get('amount') , safe=False)
            max = x.get('amount') + max
            count = count + 1
 
        average = max / count
        return JsonResponse(average, safe=False)