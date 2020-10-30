from api.v1.base import BaseModelViewSet, BaseModelWithUserViewSet
from api.v1.competitions.serializers import SeasonSerializer, CompetitionSerializer, CompetitionSectionSerializer
from competitions.models import Season, Competition, CompetitionSection


class SeasonViewSet(BaseModelWithUserViewSet):

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class CompetitionSectionViewSet(BaseModelViewSet):

    queryset = CompetitionSection.objects.all()
    serializer_class = CompetitionSectionSerializer


class CompetitionViewSet(BaseModelViewSet):

    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
