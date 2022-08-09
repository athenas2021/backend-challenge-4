from rest_framework import serializers
from revenue.models import Revenue
from .managers import RevenueManager


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = [
            # 'id',
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
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.value = validated_data.get('value', instance.value)
        RevenueManager.validate_description_month(
            self,
            validated_data['description'],
            validated_data['date'].month,
            instance.id
        )
        instance.save()
        return instance
