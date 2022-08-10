from rest_framework.views import APIView
from rest_framework.response import Response
from revenue.models import Revenue
from expenditure.models import Expenditure


class SummaryView(APIView):

    def get(self, request, month, year):
        '''
        Valor total das receitas no mês
        Valor total das despesas no mês
        Saldo final no mês
        Valor total gasto no mês em cada uma das categorias
        '''
        response = {}
        response['total_revenue'] = 0
        response['total_expenditure'] = 0
        list_expenditures_by_category = {}
        # mount category list
        for choice in Expenditure.CATEGORIES_CHOICES:
            list_expenditures_by_category[choice[1]] = 0
        queryset_revenues = Revenue.objects.filter(
            date__year=year,
            date__month=month
        )
        queryset_expenditure = Expenditure.objects.filter(
            date__year=year,
            date__month=month
        )
        for revenue in queryset_revenues:
            response['total_revenue'] += revenue.value
        for expenditure in queryset_expenditure:
            response['total_expenditure'] += expenditure.value
            if expenditure.category:
                list_expenditures_by_category[dict(Expenditure.CATEGORIES_CHOICES)[expenditure.category]] += expenditure.value

        response['final_balance'] = response['total_revenue'] - response['total_expenditure']
        response['list_expenditures_by_category'] = list_expenditures_by_category

        return Response(response)
