from .models import Revenue
from rest_framework.exceptions import ValidationError
from django.db import models


class RevenueManager(models.Manager):

    def validate_description_month(self, description, month, revenue_id=None):
        list_revenues = Revenue.objects.filter(description=description)
        if revenue_id:
            list_revenues.exclude(pk=revenue_id)
        for revenue in list_revenues:
            if month == revenue.date.month:
                raise ValidationError(f'Revenue duplicated in this month ({month})', code='duplicated')
