from django.contrib import admin

from competitions.models import Season, Competition


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass
