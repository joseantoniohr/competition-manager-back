from django.db import models

from competition_manager import choices as base_choices
from competition_manager.models import BaseModelCreation, BaseModelEdition, BaseModelDeletion


class Season(BaseModelCreation, BaseModelEdition, BaseModelDeletion):

    name = models.CharField(max_length=50, null=False, blank=False)
    is_current = models.BooleanField(default=False)  # Indicates if it is the current season
    start_year = models.PositiveSmallIntegerField(default=2020, unique=True)
    user = models.ForeignKey('auth.User', null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Season, self).save(force_insert, force_update, using, update_fields)


class CompetitionSection(BaseModelCreation, BaseModelEdition, BaseModelDeletion):

    class Meta:
        unique_together = ('name', 'season')

    name = models.CharField(max_length=100, null=False, blank=False)
    season = models.ForeignKey('competitions.Season', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Competition(BaseModelCreation, BaseModelEdition, BaseModelDeletion):

    class Meta:
        unique_together = ('name', 'season', 'section')

    name = models.CharField(max_length=100, null=False, blank=False)
    is_playoff = models.BooleanField(default=False)
    sport = models.CharField(max_length=50, choices=base_choices.SPORT_TYPE_CHOICES, null=False, blank=False)
    season = models.ForeignKey('competitions.Season', null=False, blank=False, on_delete=models.CASCADE)
    section = models.ForeignKey('competitions.CompetitionSection', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
