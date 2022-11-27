from django.db import models
from .model_match import GameMatch

class GameSpell(models):
    abilityUses = models.IntegerField
    spell1Casts = models.IntegerField
    spell2Casts = models.IntegerField
    spell3Casts = models.IntegerField
    spell4Casts = models.IntegerField

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.__class__.__name__