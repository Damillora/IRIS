from django.db import models

# Create your models here.
class CharacterManager(models.Manager):
    def comma_to_qs(self, characters_str):
        final_ids = []
        if characters_str:
            for character in characters_str.split(','):
                obj, created = self.get_or_create(romanized_name=character.strip())
                final_ids.append(obj.id)
            qs = self.get_queryset().filter(id__in=final_ids).distinct()
            return qs
        return self.none()

class Character(models.Model):
    unit = models.ForeignKey("taxonomy.Unit", on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True)
    romanized_name = models.CharField(max_length=255)
    voice_actor = models.OneToOneField("Artist", on_delete=models.PROTECT)

    class Meta:
        ordering = ['romanized_name', 'name']

    objects = CharacterManager()

    def __str__(self):
        return "["+self.unit.name+"] "+self.romanized_name+" "+" (CV: "+self.voice_actor.romanized_name+")"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)


# Create your models here.
class ArtistManager(models.Manager):
    def comma_to_qs(self, artists_str):
        final_ids = []
        if artists_str:
            for artist in artists_str.split(','):
                obj, created = self.get_or_create(romanized_name=artist.strip())
                final_ids.append(obj.id)
            qs = self.get_queryset().filter(id__in=final_ids).distinct()
            return qs
        return self.none()
    
class Artist(models.Model):
    name = models.CharField(max_length=255, blank=True)
    romanized_name = models.CharField(max_length=255)
    aliases = models.ManyToManyField("self",blank=True)

    class Meta:
        ordering = ['romanized_name', 'name']

    def __str__(self):
        return self.romanized_name
    
    objects = ArtistManager()

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
