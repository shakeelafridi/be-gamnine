import uuid

from django.db import models


class LogsMixin(models.Model):
    """Add the generic fields and relevant methods common to support mostly
    models
    """
    id = models.UUIDField(
        db_index=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """meta class for LogsMixin"""

        abstract = True

    @classmethod
    def get_objects(cls, **kwargs):
        return cls.objects.filter(**kwargs)
