from django.db import models


class NotDeletedInstances(models.Manager):

    def get_queryset(self):
        return super(NotDeletedInstances, self).get_queryset().filter(is_deleted=False)
