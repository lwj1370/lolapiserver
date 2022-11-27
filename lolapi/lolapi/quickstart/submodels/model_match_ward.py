from django.db import models
from .model_match import GameMatch

class GameWard(models):
    visionClearedPings = models.IntegerField
    visionScore = models.IntegerField
    visionWardsBoughtInGame = models.IntegerField
    wardsKilled = models.IntegerField
    wardsPlaced = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__