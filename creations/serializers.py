from rest_framework import serializers

from creations.models import Release, ReleaseCampaign, Song
from person.serializers import ArtistManySerializer

class SongOneSerializer(serializers.ModelSerializer):
    lyricist = ArtistManySerializer(many=True)
    composer = ArtistManySerializer(many=True)
    arranger = ArtistManySerializer(many=True)
    remixer = ArtistManySerializer(many=True)

    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'romanized_title',
            'english_title',
            'lyricist',
            'composer',
            'arranger',
            'singer',
            'original_song',
            'remixer',
            'bpm',
            'length',
            'genre',  
        ]


class SongManySerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'romanized_title',
            'english_title',
        ]

class ReleaseOneSerializer(serializers.ModelSerializer):
    illustrator = ArtistManySerializer(many=True)
    songs = SongManySerializer(many=True)

    class Meta:
        model = Release
        fields = [
            'id',
            'title',
            'romanized_title',
            'release_type',
            'release_date',
            'illustrator',
            'image',
            'songs',
            'link'    
        ]


class ReleaseManySerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = [
            'id',
            'title',
            'romanized_title',
            'release_type',
            'release_date',
            'image',
            'link'
        ]

class ReleaseCampaignOneSerializer(serializers.ModelSerializer):
    releases = ReleaseManySerializer(many=True)

    class Meta:
        model = ReleaseCampaign
        fields = [
            'id',
            'name',
            'releases', 
        ]


class ReleaseCampaignManySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseCampaign
        fields = [
            'id',
            'name',
        ]