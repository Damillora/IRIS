import datetime
from django.db import models

# Create your models here.

# Create your models here.


class SongManager(models.Manager):
    def newline_to_qs(self, songs_str):
        final_ids = []
        if songs_str:
            for song in songs_str.splitlines():
                obj, created = self.get_or_create(title=song.strip())
                final_ids.append(obj.id)
            qs = self.get_queryset().filter(id__in=final_ids).distinct()
            return qs
        return self.none()


class Song(models.Model):
    title = models.CharField(max_length=255)
    romanized_title = models.CharField(max_length=255, blank=True)
    english_title = models.CharField(max_length=255, blank=True)
    lyricist = models.ManyToManyField(
        "person.Artist", blank=True, related_name="written_songs")
    composer = models.ManyToManyField(
        "person.Artist", blank=True, related_name="composed_songs")
    arranger = models.ManyToManyField(
        "person.Artist", blank=True, related_name="arranged_songs")
    singer = models.ManyToManyField(
        "person.Character", blank=True, related_name="sung_songs")
    original_song = models.OneToOneField(
        "self", blank=True, null=True, on_delete=models.PROTECT)
    remixer = models.ManyToManyField(
        "person.Artist", blank=True, related_name="remixed_songs")
    bpm = models.IntegerField(blank=True, default=0)
    length = models.DurationField(
        blank=True, default=datetime.timedelta(seconds=0))
    genre = models.CharField(max_length=255, blank=True)

    objects = SongManager()

    class Meta:
        ordering = ['romanized_title', 'title']

    def __str__(self):
        return self.title


class Release(models.Model):
    class ReleaseType(models.TextChoices):
        SINGLE = "SL", "Single"
        EP = "EP", "EP"
        ALBUM = "CD", "Album"

    title = models.CharField(max_length=255, blank=True)
    romanized_title = models.CharField(max_length=255)
    release_type = models.CharField(max_length=2,
                                    choices=ReleaseType.choices,
                                    default=ReleaseType.SINGLE
                                    )
    release_date = models.DateField(blank=True, null=True)
    illustrator = models.ManyToManyField(
        "person.Artist", blank=True, related_name="illustrators")
    image = models.ImageField(blank=True)
    songs = models.ManyToManyField("Song", related_name="songs")
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['release_type', 'romanized_title', 'title']

    def __str__(self):
        return "["+self.release_type+"] "+self.romanized_title


class ReleaseCampaign(models.Model):
    name = models.CharField(max_length=255)
    releases = models.ManyToManyField("Release", related_name="releases")

    def __str__(self):
        return self.name
