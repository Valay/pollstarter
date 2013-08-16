from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
