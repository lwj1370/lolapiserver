from django.db import models
from .model_match import GameMatch

class GameDamage(models):
    damagePerMinute = models.FloatField
    totalDamageDealt = models.IntegerField
    totalDamageDealtToChampions = models.IntegerField
    totalDamageShieldedOnTeammates = models.IntegerField
    totalDamageTaken = models.IntegerField
    totalHeal = models.IntegerField
    totalHealsOnTeammates = models.IntegerField
    totalMinionsKilled = models.IntegerField
    totalTimeCCDealt = models.IntegerField
    totalTimeSpentDead = models.IntegerField
    totalUnitsHealed = models.IntegerField
    magicDamageDealt = models.IntegerField
    magicDamageDealtToChampions = models.IntegerField
    physicalDamageDealt = models.IntegerField
    physicalDamageDealtToChampions = models.IntegerField
    physicalDamageTaken = models.IntegerField
    magicDamageTaken = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__