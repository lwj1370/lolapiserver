from django.db import models
from .model_match import GameMatch

class GameItem(models):
    goldEarned = models.IntegerField
    goldSpent = models.IntegerField
    goldPerMinute = models.FloatField
    item0 = models.IntegerField
    item1 = models.IntegerField
    item2 = models.IntegerField
    item3 = models.IntegerField
    item4 = models.IntegerField
    item5 = models.IntegerField
    item6 = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.__class__.__name__