from .models import Revenue
from rest_framework.exceptions import ValidationError
from django.db import models


class RevenueManager(models.Manager):

    def validate_description_month(self):
        month = self.validated_data['date'].month
        list_revenues = Revenue.objects.filter(description=self.validated_data['description'])
        if self.instance:
            list_revenues = list_revenues.exclude(pk=self.instance.id)
        for revenue in list_revenues:
            if month == revenue.date.month:
                raise ValidationError(f'Revenue duplicated in this month ({month})', code='duplicated')
