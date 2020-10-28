from django.db import models

from competition_manager import model_managers as base_managers


class BaseModelCreation(models.Model):

    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        abstract = True


class BaseModelEdition(models.Model):

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelDeletion(models.Model):

    is_deleted = models.BooleanField(default=False)

    objects = base_managers.NotDeletedInstances()
    all_objects = models.manager.BaseManager()

    class Meta:
        abstract = True
