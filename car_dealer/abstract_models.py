from email.policy import default
from django.utils import timezone
from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SoftDeleteModel(DefaultModel):
    deleted_at = models.DateTimeField(null=True, default=None)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
