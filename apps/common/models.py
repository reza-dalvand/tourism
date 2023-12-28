from django.db import models

from apps.utils.fields.current_user import CurrentUserField


class BaseModel(models.Model):
    """A base model for every model."""

    owner = CurrentUserField(
        related_name="%(class)s_owner",
        on_delete=models.SET_NULL,
    )
    modifier = CurrentUserField(
        on_update=True,
        related_name="%(class)s_modifier",
        on_delete=models.SET_NULL,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        abstract = True
