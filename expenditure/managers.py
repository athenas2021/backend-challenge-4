from .models import Expenditure
from rest_framework.exceptions import ValidationError
from django.db import models


class ExpenditureManager(models.Manager):

    def validate_description_month(self, description, month, expenditure_id=None):
        list_expenditures = Expenditure.objects.filter(description=description)
        if expenditure_id:
            list_expenditures.exclude(pk=expenditure_id)
        for expenditure in list_expenditures:
            if month == expenditure.date.month:
                raise ValidationError(f'Expenditure duplicated in this month ({month})', code='duplicated')
