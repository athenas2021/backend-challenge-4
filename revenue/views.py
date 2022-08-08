
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

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        month = serializer.validated_data['date'].month
        list_revenues = Revenue.objects.filter(description=serializer.validated_data['description'])
        for revenue in list_revenues:
            if month == revenue.date.month:
                raise ValidationError(f'Revenue duplicated in this month ({month})', code='duplicated')
                
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
