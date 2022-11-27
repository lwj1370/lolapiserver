import os
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from riotwatcher import LolWatcher, ApiError

from .serializers import GamerMatchSerializer

from .common.utils import *

class GamerMatchViewSet(APIView):
    def post(self, request, *args, **kwargs):
        print(f'request.GET : {request.GET["nickname"] if "nickname" in request.GET else "Nickname - Not Found"}')
        print(f'request.data : {request.data["nickname"] if "nickname" in request.data else "Nickname - Not Found"}')

        result = {}
        match = result['match']
        match['matchId'] = 'Not Found'
        # result['gamer'] = {}
        match['nickname_validation'] = True

        nickname = request.data["nickname"] if "nickname" in request.data else (request.GET["nickname"] if "nickname" in request.GET else "")

        if(nickname == ""): 
            print('nickname is Empty')
            match['nickname_validation'] = False
            return Response(result)

        api_key = os.environ['LOL_API_KEY']
        
        # riotwatcher 참조
        # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
        watcher = LolWatcher(api_key)
        region = 'kr'
        
        try:
            account = watcher.summoner.by_name(region, nickname)
            matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
            matchInfo = watcher.match.by_id(region, matches[0])['info']
            
            participants = matchInfo['participants']
            participants = [participant for participant in participants if participant['puuid'] == account['puuid']]
            
            match['matchId'] = matches[0]
            match['startTime'] = datetime.fromtimestamp(matchInfo['gameStartTimestamp'] // 1000)
            match['endTime'] = datetime.fromtimestamp(matchInfo['gameEndTimestamp'] // 1000)
            match['duration'] = convertSecondsToTime(matchInfo['gameDuration'])
            result['match'].update(convertRawToGamerDictionary(participants[0]))

        except ApiError as err:
            print(f'Lol Api Request Failed : {err.response.status_code}')

        return Response(result)
    