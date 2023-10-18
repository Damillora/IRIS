from person.models import Character, Artist
from django.contrib import admin
from django import forms


# Register your models here.
admin.site.register(Character)

# Register your models here.
class ArtistForm(forms.ModelForm):
    aliases_str = forms.CharField(label='Aliases', required=False)
    class Meta:
        model = Artist
        fields = [
            'name',
            'romanized_name',
            'aliases_str',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields['aliases_str'].initial = ", ".join(x.romanized_name for x in instance.aliases.all() )

class ArtistAdmin(admin.ModelAdmin):
    form = ArtistForm
    search_fields = ['romanized_name','name']

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.6.2/tinymce.min.js',
            'tinymce-init.js'
        )
    def save_model(self, request, obj, form, change):
        aliases_str = form.cleaned_data.get('aliases_str')
        aliases = Artist.objects.comma_to_qs(aliases_str)
        if not obj.id:
            obj.save()
        obj.aliases.clear()
        obj.aliases.add(*aliases)
        obj.save()

admin.site.register(Artist, ArtistAdmin)