from email.policy import default
from car_dealer.abstract_models import SoftDeleteModel
from django.db import models
import uuid


from locations.models import Location
from brands.models import Brand


class Car(SoftDeleteModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    codename = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    def __str__(self):
        return self.codename
