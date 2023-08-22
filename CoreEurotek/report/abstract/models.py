from django.db import models
import uuid


class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
