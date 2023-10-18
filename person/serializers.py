from rest_framework import serializers

from person.models import Artist, Character
from taxonomy.serializers import UnitManySerializer

class ArtistManySerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'romanized_name',
        ]

class ArtistOneSerializer(serializers.ModelSerializer):
    aliases = ArtistManySerializer(many=True)

    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'romanized_name',
            'aliases'
        ]

class CharacterManySerializer(serializers.ModelSerializer):
    voice_actor = ArtistManySerializer()
    unit = UnitManySerializer()
    
    class Meta:
        model = Character
        fields = [
            'id',
            'unit',
            'name',
            'romanized_name',
            'voice_actor',
        ]

class CharacterOneSerializer(serializers.ModelSerializer):
    unit = UnitManySerializer()

    class Meta:
        model = Character
        fields = [
            'id',
            'unit',
            'name',
            'romanized_name',
        ]