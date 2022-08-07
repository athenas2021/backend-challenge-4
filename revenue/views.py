from rest_framework import viewsets, status
from revenue.models import Revenue
from revenue.serializers import RevenueSerializer
from rest_framework.response import Response


class RevenueViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows revenue to be created, listed, viewed or edited.
    '''
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        '''
        TODO - Colocar aqui validação para regra:
        A API não deve permitir o cadastro de depesas duplicadas
        (contendo a mesma descrição, dentro do mesmo mês)
        '''
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)