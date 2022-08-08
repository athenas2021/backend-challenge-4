from rest_framework import viewsets, status
from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view


class ExpenditureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows expenditure to be created, listed, viewed or edited.
    '''
    queryset = Expenditure.objects.all().order_by('-id')
    serializer_class = ExpenditureSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        month = serializer.validated_data['date'].month
        list_expenditures = Expenditure.objects.filter(description=serializer.validated_data['description'])
        for expenditure in list_expenditures:
            if month == expenditure.date.month:
                raise ValidationError(f'Expenditure duplicated in this month ({month})', code='duplicated')
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @api_view(['PUT'])
    # def update(self, request, *args, **kwargs):
    #     print('entrei')
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     month = serializer.validated_data['date'].month
    #     list_expenditures = Expenditure.objects.filter(description=serializer.validated_data['description'])
    #     for expenditure in list_expenditures:
    #         if month == expenditure.date.month:
    #             raise ValidationError(f'Expenditure duplicated in this month ({month})', code='duplicated')
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)