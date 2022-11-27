from django.db import models
from .model_match import GameMatch

class GameTurret(models):
    firstTowerAssist = models.BooleanField
    firstTowerKill = models.BooleanField
    turretKills = models.IntegerField
    turretTakedowns = models.IntegerField
    turretsLost = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__