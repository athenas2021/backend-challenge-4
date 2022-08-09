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
        ExpenditureManager.validate_description_month(
            self,
            validated_data['description'],
            validated_data['date'].month
        )
        return Expenditure.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.value = validated_data.get('value', instance.value)
        instance.category = validated_data.get('category', instance.category)
        ExpenditureManager.validate_description_month(
            self,
            validated_data['description'],
            validated_data['date'].month,
            instance.id
        )
        instance.save()
        return instance
