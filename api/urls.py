from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'song', views.SongViewSet)
router.register(r'release', views.ReleaseViewSet)
router.register(r'release-campaign', views.ReleaseCampaignViewSet)
router.register(r'artist', views.ArtistViewSet)
router.register(r'character', views.CharacterViewSet)
router.register(r'area', views.AreaViewSet)
router.register(r'unit', views.UnitViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
