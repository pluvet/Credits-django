from datetime import datetime, timedelta

from .models import Credit


def yesterday(funcion_b):

    def wrap(self, request):
        

        date = datetime.now().date() - timedelta(days=1)


        credits = Credit.objects.filter(date__gte = date.strftime("%Y-%m-%d") + ' 00:00:00.882454-05') \
                                .filter(date__lte = date.strftime("%Y-%m-%d") + ' 23:59:59.882454-05').values()    
        credits = list(credits)

        return funcion_b(self, request, credits)

    return wrap