from .models import Expenditure
from rest_framework.exceptions import ValidationError
from django.db import models


class ExpenditureManager(models.Manager):

    def validate_description_month(self):
        month = self.validated_data['date'].month
        list_expenditures = Expenditure.objects.filter(description=self.validated_data['description'])
        if self.instance:
            list_expenditures = list_expenditures.exclude(pk=self.instance.id)
        for expenditure in list_expenditures:
            if month == expenditure.date.month:
                raise ValidationError(f'Expenditure duplicated in this month ({month})', code='duplicated')
