from django.db import models
from .model_match import GameMatch

class GameInfo(models.Model):
    summonerName = models.CharField(max_length=100)
    summoverLevel = models.IntegerField(max_length=5)
    champLevel = models.IntegerField(max_length=2)
    championId = models.IntegerField(max_length=10)
    championName = models.CharField(max_length=100)
    lane = models.CharField(max_length=10)
    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__
