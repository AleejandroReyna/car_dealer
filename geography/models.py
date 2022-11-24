from car_dealer.abstract_models import SoftDeleteModel


from django.db import models


class Country(SoftDeleteModel):
    name = models.CharField(unique=True, max_length=30)


class State(SoftDeleteModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')


class City(SoftDeleteModel):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'state')
