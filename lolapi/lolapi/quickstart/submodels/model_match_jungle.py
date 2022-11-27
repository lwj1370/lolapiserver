from django.db import models
from .model_match import GameMatch

class GameJungle(models):
    baronTakedowns = models.IntegerField(max_length=10)
    dragonTakedowns = models.IntegerField(max_length=10)
    elderDragonMultikills = models.IntegerField(max_length=10)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__
