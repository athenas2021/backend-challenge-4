from rest_framework import serializers
from revenue.models import Revenue


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = [
            # 'id',
            'description',
            'value',
            'date',
        ]
