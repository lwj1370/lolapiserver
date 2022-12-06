from django.db import models
from .model_match import GameMatch

class GamerWinRate(models.Model):
    win = models.BooleanField(default=False)
    gameEndedInEarlySurrender = models.BooleanField(default=False)
    gameEndedInSurrender = models.BooleanField(default=False)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__()} : setJsonData Start')

        self.win = json['win']
        self.gameEndedInEarlySurrender = json['gameEndedInEarlySurrender']
        self.gameEndedInSurrender = json['gameEndedInSurrender']

        print(f'{self.__str__()} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__