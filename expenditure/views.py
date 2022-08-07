from rest_framework import viewsets
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer


class ExpenditureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows expenditure to be created, listed, viewed or edited.
    '''
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer