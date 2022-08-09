from rest_framework import viewsets, status
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ExpenditureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows expenditure to be created, listed, viewed or edited.
    '''
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer
