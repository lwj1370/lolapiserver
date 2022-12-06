from django.db import models
from .model_match import GameMatch

class GameTurret(models.Model):
    firstTowerAssist = models.BooleanField(default=False)
    firstTowerKill = models.BooleanField(default=False)
    turretKills = models.IntegerField(default=0)
    turretTakedowns = models.IntegerField(default=0)
    turretsLost = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__()} : setJsonData Start')

        self.firstTowerAssist = json['firstTowerAssist']
        self.firstTowerKill = json['firstTowerKill']
        self.turretKills = json['turretKills']
        self.turretTakedowns = json['turretTakedowns']
        self.turretsLost = json['turretsLost']

        print(f'{self.__str__()} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__