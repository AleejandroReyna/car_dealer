from car_dealer.abstract_models import SoftDeleteModel
from django.db import models


from geography.models import City


class Location(SoftDeleteModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



