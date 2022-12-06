from django.db import models
from .model_match import GameMatch

class GameInfo(models.Model):
    summonerName = models.CharField(max_length=100)
    summonerLevel = models.IntegerField(default=0)
    champLevel = models.IntegerField(default=0)
    championId = models.IntegerField(default=0)
    championName = models.CharField(max_length=100)
    lane = models.CharField(max_length=10)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__()} : setJsonData Start')

        self.summonerName = json['summonerName']
        self.summonerLevel = json['summonerLevel']
        self.champLevel = json['champLevel']
        self.championId = json['championId']
        self.championName = json['championName']
        self.lane = json['lane']

        print(f'{self.__str__()} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__
