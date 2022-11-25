from django.db import models

class ProGamer(models.Model):
    gamer_nickname = models.CharField(max_length = 100)
    puuid = models.CharField(max_length = 200)
    team_name = models.CharField(max_length = 50)
    lane_position = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.gamer_nickname