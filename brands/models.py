from car_dealer.abstract_models import SoftDeleteModel
from django.db import models


class Brand(SoftDeleteModel):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
