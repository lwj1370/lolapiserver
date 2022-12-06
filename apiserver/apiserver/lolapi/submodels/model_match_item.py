from django.db import models
from .model_match import GameMatch

class GameItem(models.Model):
    goldEarned = models.IntegerField(default=0)
    goldSpent = models.IntegerField(default=0)
    goldPerMinute = models.FloatField(default=0.0)
    item0 = models.IntegerField(default=0)
    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)
    item4 = models.IntegerField(default=0)
    item5 = models.IntegerField(default=0)
    item6 = models.IntegerField(default=0)

    match = models.ForeignKey(GameMatch, on_delete=models.CASCADE)
    
    def setJsonData(self, json):
        print(f'{self.__str__()} : setJsonData Start')

        self.goldEarned = json['goldEarned']
        self.goldSpent = json['goldSpent']
        self.goldPerMinute = json['goldPerMinute']
        self.item0 = json['item0']
        self.item1 = json['item1']
        self.item2 = json['item2']
        self.item3 = json['item3']
        self.item4 = json['item4']
        self.item5 = json['item5']
        self.item6 = json['item6']

        print(f'{self.__str__()} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__