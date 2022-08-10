
from rest_framework import viewsets
from revenue.models import Revenue
from revenue.serializers import RevenueSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from datetime import date


class RevenueViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows revenue to be created, listed, viewed or edited.
    '''
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSerializer

    def list(self, request):
        queryset = self.get_queryset()
        filter_description = request.GET.get('description', None)
        if filter_description:
            queryset = queryset.filter(description=filter_description)
        queryset = self.paginate_queryset(queryset)
        serializer = RevenueSerializer(queryset, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

class RevenueByMonthView(ListAPIView):

    serializer_class = RevenueSerializer

    def get_queryset(self):
        # TODO - passar essa validação para manager
        month = self.kwargs['month']
        year = self.kwargs['year']
        if month not in range(1, 13):
            raise ValidationError(f'Month not valid({month})', code='month-invalid')
        if year not in range(2000, (date.today().year)+1):
            raise ValidationError(f'Year not valid ({year})', code='year-invalid')

        return (
            Revenue.objects.filter(
                date__year=year,
                date__month=month
            )
        )

