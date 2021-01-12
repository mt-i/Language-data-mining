from phrase.models import Phrase, ComplexPhrase, FreePull
from django.contrib import admin

# Register your models here.
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['tshivenda', 'english']

class ComplexPhraseAdmin(admin.ModelAdmin):
    list_display = ['tshivenda', 'english']


class FreePullAdmin(admin.ModelAdmin):
    list_display = ['tshivenda', 'english']

admin.site.register(ComplexPhrase,ComplexPhraseAdmin)
admin.site.register(Phrase,PhraseAdmin)
admin.site.register(FreePull,FreePullAdmin)
