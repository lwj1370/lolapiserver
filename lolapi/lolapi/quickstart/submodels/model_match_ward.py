from django.db import models
from .model_match import GameMatch

class GameWard(models.Model):
    visionClearedPings = models.IntegerField(default=0)
    visionScore = models.IntegerField(default=0)
    visionWardsBoughtInGame = models.IntegerField(default=0)
    wardsKilled = models.IntegerField(default=0)
    wardsPlaced = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__} : setJsonData Start')

        self.visionClearedPings = json['visionClearedPings']
        self.visionScore = json['visionScore']
        self.visionWardsBoughtInGame = json['visionWardsBoughtInGame']
        self.wardsKilled = json['wardsKilled']
        self.wardsPlaced = json['wardsPlaced']

        print(f'{self.__str__} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__