from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Comment(BaseModel):
    """used Comment as a common model for hotels and tours app"""

    body = models.TextField(_("body"))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
