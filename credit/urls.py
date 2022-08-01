from django.urls import path
from .views import AmountGeneratedView, CreditView

urlpatterns = [
    path('credits/', CreditView.as_view(), name='credits_list'),
    path('credits/<int:id>', CreditView.as_view(), name='credits_process'),
    path('credits/amount', CreditView.AmountGeneratedView.as_view(), name='credits_process'),
    path('credits/average', CreditView.AmountAverageView.as_view(), name='credits_average'),
    path('credits/interest', CreditView.InterestAverageView.as_view(), name='interest_Average'),

    path('amount', AmountGeneratedView.as_view(), name='calculate_process'),
    path('average', AmountGeneratedView.as_view(), name='calculate_process')
]
