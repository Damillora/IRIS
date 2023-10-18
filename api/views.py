
from creations.serializers import ReleaseCampaignManySerializer, ReleaseCampaignOneSerializer, ReleaseManySerializer, ReleaseOneSerializer, SongManySerializer, SongOneSerializer
from creations.models import Release, ReleaseCampaign, Song
from rest_framework import viewsets
from rest_framework import permissions
from person.models import Artist, Character

from person.serializers import ArtistManySerializer, ArtistOneSerializer, CharacterManySerializer, CharacterOneSerializer
from taxonomy.models import Area, Unit
from taxonomy.serializers import AreaManySerializer, AreaOneSerializer, UnitManySerializer, UnitOneSerializer

class SongViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SongOneSerializer
        else:
            return SongManySerializer
        
    queryset = Song.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

class ReleaseViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ReleaseOneSerializer
        else:
            return ReleaseManySerializer
        
    queryset = Release.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

class ReleaseCampaignViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ReleaseCampaignOneSerializer
        else:
            return ReleaseCampaignManySerializer
        
    queryset = ReleaseCampaign.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

class ArtistViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArtistOneSerializer
        else:
            return ArtistManySerializer
        
    queryset = Artist.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

class CharacterViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CharacterOneSerializer
        else:
            return CharacterManySerializer
        
    queryset = Character.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
        
class AreaViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AreaOneSerializer
        else:
            return AreaManySerializer
        
    queryset = Area.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
        
class UnitViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UnitOneSerializer
        else:
            return UnitManySerializer
        
    queryset = Unit.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
        
