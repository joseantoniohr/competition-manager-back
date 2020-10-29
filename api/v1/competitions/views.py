from api.v1.base import BaseModelViewSet, BaseModelWithUserViewSet
from api.v1.competitions.serializers import SeasonSerializer, CompetitionSerializer
from competitions.models import Season, Competition


class SeasonViewSet(BaseModelWithUserViewSet):

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class CompetitionViewSet(BaseModelViewSet):

    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
