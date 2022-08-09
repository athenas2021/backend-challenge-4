from rest_framework import serializers
from expenditure.models import Expenditure
from .managers import ExpenditureManager


class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = [
            'id',
            'description',
            'value',
            'date',
            'category',
        ]

    def create(self, validated_data):
        ExpenditureManager.validate_description_month(self)
        return Expenditure.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        ExpenditureManager.validate_description_month(self)
        instance.save()
        return instance
