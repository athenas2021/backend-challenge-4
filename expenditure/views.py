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
        filter_description = request.GET.get('description', None)
        if filter_description:
            queryset = queryset.filter(description=filter_description)
        queryset = self.paginate_queryset(queryset)
        serializer = ExpenditureSerializer(queryset, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)


class ExpenditureByMonthView(ListAPIView):

    serializer_class = ExpenditureSerializer

    def get_queryset(self):
        # TODO - passar essa validação para manager
        month = self.kwargs['month']
        year = self.kwargs['year']
        if month not in range(1,13):
            raise ValidationError(f'Month not valid ({month})', code='month-invalid')
        if year not in range(2000, (date.today().year)+1):
            raise ValidationError(f'Year not valid ({year})', code='year-invalid')

        queryset = Expenditure.objects.filter(
            date__year=year,
            date__month=month
        )
        return queryset
