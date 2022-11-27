from django.db import models
from .model_match import GameMatch

class GamerWinRate(models):
    win = models.BooleanField
    gameEndedInEarlySurrender = models.BooleanField
    gameEndedInSurrender = models.BooleanField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__