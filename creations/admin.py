from django import forms
from django.contrib import admin
from .models import Release, ReleaseCampaign, Song
from person.models import Artist, Character

# Register your models here.
class SongForm(forms.ModelForm):
    lyricist_str = forms.CharField(label='Lyricists', required=False)
    composer_str = forms.CharField(label='Composers', required=False)
    arranger_str = forms.CharField(label='Arrangers', required=False)
    singer_str = forms.CharField(label='Singers', required=False)
    remixer_str = forms.CharField(label='Remixers', required=False)

    class Meta:
        model = Song
        fields = [
            'title',
            'romanized_title',
            'english_title',
            'lyricist_str',
            'composer_str',
            'arranger_str',
            'singer_str',
            'original_song',
            'remixer_str',
            'bpm',
            'length',
            'genre',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields['lyricist_str'].initial = ', '.join(
                x.romanized_name for x in instance.lyricist.all())
            self.fields['composer_str'].initial = ', '.join(
                x.romanized_name for x in instance.composer.all())
            self.fields['arranger_str'].initial = ', '.join(
                x.romanized_name for x in instance.arranger.all())
            self.fields['singer_str'].initial = ', '.join(
                x.romanized_name for x in instance.singer.all())
            self.fields['remixer_str'].initial = ', '.join(
                x.romanized_name for x in instance.remixer.all())


class SongAdmin(admin.ModelAdmin):
    form = SongForm
    search_fields = ['romanized_title', 'title']

    def save_model(self, request, obj, form, change):
        lyricist_str = form.cleaned_data.get('lyricist_str')
        composer_str = form.cleaned_data.get('composer_str')
        arranger_str = form.cleaned_data.get('arranger_str')
        singer_str = form.cleaned_data.get('singer_str')
        remixer_str = form.cleaned_data.get('remixer_str')
        lyricist = Artist.objects.comma_to_qs(lyricist_str)
        composer = Artist.objects.comma_to_qs(composer_str)
        arranger = Artist.objects.comma_to_qs(arranger_str)
        singer = Character.objects.comma_to_qs(singer_str)
        remixer = Artist.objects.comma_to_qs(remixer_str)
        if not obj.id:
            obj.save()
        obj.lyricist.clear()
        obj.lyricist.add(*lyricist)
        obj.composer.clear()
        obj.composer.add(*composer)
        obj.arranger.clear()
        obj.arranger.add(*arranger)
        obj.singer.clear()
        obj.singer.add(*singer)
        obj.remixer.clear()
        obj.remixer.add(*remixer)
        obj.save()




admin.site.register(Song, SongAdmin)

class ReleaseForm(forms.ModelForm):
    songs_str = forms.CharField(label='Songs', widget=forms.Textarea, required=False)
    illustrator_str = forms.CharField(label='Illustrators', required=False)

    class Meta:
        model = Release
        fields = [
            'title',
            'romanized_title',
            'release_type',
            'release_date',
            'illustrator_str',
            'image',
            'songs_str',
            'link'    
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields['songs_str'].initial = '\n'.join(
                x.title for x in instance.songs.all())
            self.fields['illustrator_str'].initial = '\n'.join(
                x.romanized_name for x in instance.illustrator.all())
    
class ReleaseAdmin(admin.ModelAdmin):
    form = ReleaseForm
    search_fields = ['romanized_title', 'title']

    def save_model(self, request, obj, form, change):
        song_str = form.cleaned_data.get('songs_str')
        illustrator_str = form.cleaned_data.get('illustrator_str')
        songs = Song.objects.newline_to_qs(song_str)
        illustrators = Artist.objects.comma_to_qs(illustrator_str)
        if not obj.id:
            obj.save()
        obj.songs.clear()
        obj.songs.add(*songs)
        obj.illustrator.clear()
        obj.illustrator.add(*illustrators)
        obj.save()

admin.site.register(Release, ReleaseAdmin)

admin.site.register(ReleaseCampaign)