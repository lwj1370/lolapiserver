from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from riotwatcher import LolWatcher, ApiError

from .serializers import GamerMatchSerializer

from .common.utils import convertRawToGamerDictionary

class GamerMatchViewSet(APIView):
    def post(self, request, *args, **kwargs):
        api_key = 'RGAPI-3d62bc5d-f4ed-48c6-a550-eadc69d5cdfb'
        # riotwatcher 참조
        # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
        watcher = LolWatcher(api_key)
        region = 'kr'
        result = {}
        result['matchId'] = 'Not Found'
        result['gamer'] = {}

        try:
            account = watcher.summoner.by_name(region, 'SKT T1 Faker')
            matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
            lastMatch = matches[0]
            participants = watcher.match.by_id(region, lastMatch)['info']['participants']
            participants = [participant for participant in participants if participant['puuid'] == account['puuid']]
            result['matchId'] = lastMatch
            result['gamer'].update(convertRawToGamerDictionary(participants[0]))

        except ApiError as err:
            print(f'Api Failed : {err.response.status_code}')

        return Response(result)
    