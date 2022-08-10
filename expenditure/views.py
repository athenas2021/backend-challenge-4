from rest_framework import viewsets
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
# from datatables.models import DataTables
from datetime import date



class ExpenditureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows expenditure to be created, listed, viewed or edited.
    '''
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer

    def list(self, request):
        queryset = self.get_queryset()
        filter_description = request.GET.getlist('description', None)
        if len(filter_description) > 0:
            queryset = queryset.filter(description__in=filter_description)
        queryset = self.paginate_queryset(queryset)
        serializer = ExpenditureSerializer(queryset, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

    def searchExpenditureByMonth(self, month, year):
        # TODO - passar essa validação para manager
        print('month->', month)
        if month not in range(1,13):
            raise ValidationError(f'Month not valid ({month})', code='month-invalid')
        if year not in range(2000, (date.today().year)+1):
            raise ValidationError(f'Year not valid ({year})', code='year-invalid')

        queryset = Expenditure.objects.filter(
            date__year=year,
            date__month=month   
        )
        print('queryset->', queryset)
        queryset = ExpenditureViewSet.paginate_queryset(self, queryset)
        if queryset is not None:
            serializer = ExpenditureViewSet.get_serializer(queryset, many=True)
            return ExpenditureViewSet.get_paginated_response(serializer.data)

class ExpenditureByMonthView(ListAPIView):
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer
    def list(self, request):
        print('teste')
        print(self, request)
