from rest_framework import serializers
from revenue.models import Revenue
from .managers import RevenueManager


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = [
            'id',
            'description',
            'value',
            'date',
        ]

    def create(self, validated_data):
        RevenueManager.validate_description_month(
            self,
            validated_data['description'],
            validated_data['date'].month
        )
        return Revenue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        RevenueManager.validate_description_month(
            self,
            validated_data['description'],
            validated_data['date'].month,
            instance.id
        )
        instance.save()
        return instance
