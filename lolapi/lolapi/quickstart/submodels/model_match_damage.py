from django.db import models
from .model_match import GameMatch

class GameDamage(models.Model):
    damagePerMinute = models.FloatField(default=0.0)
    totalDamageDealt = models.IntegerField(default=0)
    totalDamageDealtToChampions = models.IntegerField(default=0)
    totalDamageShieldedOnTeammates = models.IntegerField(default=0)
    totalDamageTaken = models.IntegerField(default=0)
    totalHeal = models.IntegerField(default=0)
    totalHealsOnTeammates = models.IntegerField(default=0)
    totalMinionsKilled = models.IntegerField(default=0)
    totalTimeCCDealt = models.IntegerField(default=0)
    totalTimeSpentDead = models.IntegerField(default=0)
    totalUnitsHealed = models.IntegerField(default=0)
    magicDamageDealt = models.IntegerField(default=0)
    magicDamageDealtToChampions = models.IntegerField(default=0)
    physicalDamageDealt = models.IntegerField(default=0)
    physicalDamageDealtToChampions = models.IntegerField(default=0)
    physicalDamageTaken = models.IntegerField(default=0)
    magicDamageTaken = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__} : setJsonData Start')

        self.damagePerMinute = json['damagePerMinute']
        self.totalDamageDealt = json['totalDamageDealt']
        self.totalDamageDealtToChampions = json['totalDamageDealtToChampions']
        self.totalDamageShieldedOnTeammates = json['totalDamageShieldedOnTeammates']
        self.totalDamageTaken = json['totalDamageTaken']
        self.totalHeal = json['totalHeal']
        self.totalHealsOnTeammates = json['totalHealsOnTeammates']
        self.totalMinionsKilled = json['totalMinionsKilled']
        self.totalTimeCCDealt = json['totalTimeCCDealt']
        self.totalTimeSpentDead = json['totalTimeSpentDead']
        self.totalUnitsHealed = json['totalUnitsHealed']
        self.magicDamageDealt = json['magicDamageDealt']
        self.magicDamageDealtToChampions = json['magicDamageDealtToChampions']
        self.magicDamageTaken = json['physicalDamageTaken']
        self.physicalDamageDealt = json['physicalDamageDealt']
        self.physicalDamageDealtToChampions = json['physicalDamageDealtToChampions']
        self.physicalDamageTaken = json['physicalDamageTaken']

        print(f'{self.__str__} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__