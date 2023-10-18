from rest_framework import serializers

from taxonomy.models import Area, Unit

class AreaManySerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id',
            'name',
            'logo',
        ]

class AreaOneSerializer(serializers.ModelSerializer):
    aliases = AreaManySerializer(many=True)

    class Meta:
        model = Area
        fields = [
            'id',
            'name',
            'description',
            'logo',
        ]

class UnitManySerializer(serializers.ModelSerializer):
    area = AreaManySerializer()

    class Meta:
        model = Unit
        fields = [
            'id',
            'area',
            'name',
        ]

class UnitOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'id',
            'area',
            'name',
            'description',
        ]