from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from lolapi.quickstart.serializers import UserSerializer, GroupSerializer
from riotwatcher import LolWatcher, ApiError

from .common.utils import convertRawToGamerDictionary

class UserViewSet(APIView):
    def post(self, request, *args, **kwargs):
        api_key = 'RGAPI-b211dfaf-81fd-479b-a77d-268bf748009c'
        # riotwatcher 참조
        # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
        watcher = LolWatcher(api_key)
        region = 'kr'
        account = watcher.summoner.by_name(region, 'SKT T1 Faker')
        matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
        lastMatch = matches[0]
        participants = watcher.match.by_id(region, lastMatch)['info']['participants']
        participants = [participant for participant in participants if participant['puuid'] == account['puuid']]

        result = {}
        result['matchId'] = lastMatch
        result['gamer'] = {}
        
        result['gamer'].update(convertRawToGamerDictionary(participants[0]))

        return Response(result)
    