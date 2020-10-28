from django.utils.translation import ugettext_lazy as _


# ############################################################################################### #
# #########################                  SPORT TYPES                ######################### #
# ############################################################################################### #
SPORT_FOOTBALL = "football"
SPORT_BASKETBALL = "basketball"
SPORT_HANDBALL = "handball"
SPORT_RUGBY = "rugby"
SPORT_WATER_POLO = "waterpolo"
SPORT_TENNIS = "tennis"
SPORT_VOLLEYBALL = "volleyball"

SPORT_TYPE_CHOICES = (
    (SPORT_FOOTBALL, _("Football")),
    (SPORT_BASKETBALL, _("Basketball")),
    (SPORT_HANDBALL, _("Handball")),
    (SPORT_RUGBY, _("Rugby")),
    (SPORT_WATER_POLO, _("Waterpolo")),
    (SPORT_TENNIS, _("Tennis")),
    (SPORT_VOLLEYBALL, _("Volleyball")),
)
# ############################################################################################### #
