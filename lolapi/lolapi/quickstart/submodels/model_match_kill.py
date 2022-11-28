from django.db import models
from .model_match import GameMatch

class GameKill(models.Model):
    firstBloodAssist = models.BooleanField(default=False)
    firstBloodKill = models.BooleanField(default=False)
    assists = models.IntegerField(default=0)
    largestMultiKill = models.IntegerField(default=0)
    participantId = models.IntegerField(default=0)
    doubleKills = models.IntegerField(default=0)
    tripleKills = models.IntegerField(default=0)
    quadraKills = models.IntegerField(default=0)
    pentaKills = models.IntegerField(default=0)
    unrealKills = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    kda = models.FloatField(default=0.0)
    dragonKills = models.IntegerField(default=0)
    baronKills = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__} : setJsonData Start')

        self.firstBloodAssist = json['firstBloodAssist']
        self.firstBloodKill = json['firstBloodKill']
        self.assists = json['assists']
        self.largestMultiKill = json['largestMultiKill']
        self.participantId = json['participantId']
        self.doubleKills = json['doubleKills']
        self.tripleKills = json['tripleKills']
        self.quadraKills = json['quadraKills']
        self.pentaKills = json['pentaKills']
        self.unrealKills = json['unrealKills']
        self.kills = json['kills']
        self.deaths = json['deaths']
        self.kda = json['kda']
        self.dragonKills = json['dragonKills']
        self.baronKills = json['baronKills']

        print(f'{self.__str__} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__
