from django.db import models
from .model_match import GameMatch

class GameJungle(models.Model):
    baronTakedowns = models.IntegerField(default=0)
    dragonTakedowns = models.IntegerField(default=0)
    elderDragonMultikills = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__()} : setJsonData Start')

        self.baronTakedowns = json['baronTakedowns']
        self.dragonTakedowns = json['dragonTakedowns']
        self.elderDragonMultikills = json['elderDragonMultikills']
        
        print(f'{self.__str__()} : setJsonData End')
        

    def __str__(self) -> str:
        return self.__class__.__name__
