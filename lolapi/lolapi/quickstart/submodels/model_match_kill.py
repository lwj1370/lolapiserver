from django.db import models
from .model_match import GameMatch

class GameKill(models):
    firstBloodAssist = models.BooleanField
    firstBloodKill = models.BooleanField
    assists = models.IntegerField
    largestMultiKill = models.IntegerField
    participantId = models.IntegerField
    doubleKills = models.IntegerField
    tripleKills = models.IntegerField
    quadraKills = models.IntegerField
    pentaKills = models.IntegerField
    unrealKills = models.IntegerField
    kills = models.IntegerField
    deaths = models.IntegerField
    kda = models.FloatField
    dragonKills = models.IntegerField
    baronKills = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__
