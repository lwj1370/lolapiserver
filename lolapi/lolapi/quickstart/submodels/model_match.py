from django.db import models
from django.utils import timezone
from .model_pro_gamer import ProGamer

class GameMatch(models.Model):
    matchId = models.CharField(max_length=15)
    nickaname_validation = models.BooleanField(default=False)
    startTime = models.DateTimeField(blank=False)
    endTime = models.DateTimeField(blank=False)
    duration = models.CharField(max_length=20)
    requested_time = models.DateTimeField(default=timezone.now)
    
    pro_gamer = models.ForeignKey(ProGamer, on_delete=models.CASCADE)

    def setJsonData(self, json):
        print(f'{self.__str__} : setJsonData Start')

        self.matchId = json['matchId']
        self.nickaname_validation = json['nickname_validation']
        self.startTime = json['startTime']
        self.endTime = json['endTime']
        self.duration = json['duration']

        print(f'{self.__str__} : setJsonData End')

    def __str__(self) -> str:
        return self.__class__.__name__