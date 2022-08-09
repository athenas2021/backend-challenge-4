from rest_framework import viewsets
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer
# from datatables.models import DataTables


class ExpenditureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows expenditure to be created, listed, viewed or edited.
    '''
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer

    def list(self, request):
        queryset = self.get_queryset()
        print('queryset->', queryset)
        filter_description = request.GET.getlist('description', None)
        if len(filter_description) > 0:
            queryset = queryset.filter(description__in=filter_description)
        queryset = self.paginate_queryset(queryset)
        serializer = ExpenditureSerializer(queryset, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)
