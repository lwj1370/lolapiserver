import os
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from riotwatcher import LolWatcher, ApiError

from .serializers import GamerMatchSerializer

from .common.utils import convertRawToGamerDictionary

class GamerMatchViewSet(APIView):
    def post(self, request, *args, **kwargs):
        print(f'request.GET : {request.GET["nickname"] if "nickname" in request.GET else "Nickname - Not Found"}')
        print(f'request.data : {request.data["nickname"] if "nickname" in request.data else "Nickname - Not Found"}')

        result = {}
        result['matchId'] = 'Not Found'
        result['gamer'] = {}
        result['nickname_validation'] = True

        nickname = request.data["nickname"] if "nickname" in request.data else (request.GET["nickname"] if "nickname" in request.GET else "")

        if(nickname == ""): 
            result['nickname_validation'] = False
            return Response(result)

        api_key = os.environ['LOL_API_KEY']
        
        # riotwatcher 참조
        # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
        watcher = LolWatcher(api_key)
        region = 'kr'
        
        try:
            account = watcher.summoner.by_name(region, nickname)
            matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
            lastMatch = matches[0]
            participants = watcher.match.by_id(region, lastMatch)['info']['participants']
            participants = [participant for participant in participants if participant['puuid'] == account['puuid']]
            result['matchId'] = lastMatch
            result['gamer'].update(convertRawToGamerDictionary(participants[0]))

        except ApiError as err:
            print(f'Api Failed : {err.response.status_code}')

        return Response(result)
    