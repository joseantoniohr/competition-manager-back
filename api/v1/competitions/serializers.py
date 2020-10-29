from rest_framework import serializers

from competitions.models import Season, Competition


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = ['id', 'name', 'is_current', 'start_year']


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = ['id', 'name', 'is_playoff', 'sport']
