
from rest_framework import viewsets
from revenue.models import Revenue
from revenue.serializers import RevenueSerializer


class RevenueViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows revenue to be created, listed, viewed or edited.
    '''
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSerializer
