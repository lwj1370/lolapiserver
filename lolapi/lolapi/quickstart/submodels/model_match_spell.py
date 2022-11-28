from django.db import models
from .model_match import GameMatch

class GameSpell(models.Model):
    abilityUses = models.IntegerField(default=0)
    spell1Casts = models.IntegerField(default=0)
    spell2Casts = models.IntegerField(default=0)
    spell3Casts = models.IntegerField(default=0)
    spell4Casts = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__} : setJsonData Start')

        self.abilityUses = json['abilityUses']
        self.spell1Casts = json['spell1Casts']
        self.spell2Casts = json['spell2Casts']
        self.spell3Casts = json['spell3Casts']
        self.spell4Casts = json['spell4Casts']

        print(f'{self.__str__} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__