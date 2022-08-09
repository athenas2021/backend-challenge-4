
from rest_framework import viewsets, status
from revenue.models import Revenue
from revenue.serializers import RevenueSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class RevenueViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows revenue to be created, listed, viewed or edited.
    '''
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSerializer

