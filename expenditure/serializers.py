from rest_framework import serializers
from expenditure.models import Expenditure


class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = [
            'description',
            'value',
            'date'
        ]