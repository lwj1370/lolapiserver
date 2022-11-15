from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from lolapi.quickstart.serializers import UserSerializer, GroupSerializer
from riotwatcher import LolWatcher, ApiError

class UserViewSet(APIView):
    def post(self, request, *args, **kwargs):
        api_key = 'RGAPI-d94a8dea-e7d9-4ad1-a066-51e75661d0a0'
        # riotwatcher 참조
        # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
        watcher = LolWatcher(api_key)
        region = 'kr'
        account = watcher.summoner.by_name(region, 'SKT T1 Faker')
        matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
        lastMatch = matches[0]
        participants = watcher.match.by_id(region, lastMatch)['info']['participants']

        result = {}
        result['matchId'] = lastMatch
        result['reformedParticipants'] = []
        reformedParticipants = result['reformedParticipants']
        for participant in participants:

            challenges = participant['challenges']
            data = {}

            # 유저 정보
            info = {}
            info['summonerName'] = participant['summonerName']
            info['summonerLevel'] = participant['summonerLevel']
            info['champLevel'] = participant['champLevel']
            info['championId'] = participant['championId']
            info['championName'] = participant['championName']
            info['lane'] = participant['lane']
            
            data['info'] = info

            # jungle 정보
            jungle = {}
            jungle['baronTakedowns'] = challenges['baronTakedowns']
            jungle['dragonTakedowns'] = challenges['dragonTakedowns']
            jungle['elderDragonMultikills'] = challenges['elderDragonMultikills']

            data['jungle'] = jungle

            # item/gold 결과
            item = {}
            item['goldEarned'] = participant['goldEarned']
            item['goldSpent'] = participant['goldSpent']
            item['goldPerMinute'] = challenges['goldPerMinute']
            item['item0'] = participant['item0']
            item['item1'] = participant['item1']
            item['item2'] = participant['item2']
            item['item3'] = participant['item3']
            item['item4'] = participant['item4']
            item['item5'] = participant['item5']
            item['item6'] = participant['item6']
            
            data['item'] = item

            # kill 결과 정보
            kill = {}
            
            kill['firstBloodAssist'] = participant['firstBloodAssist']
            kill['firstBloodKill'] = participant['firstBloodKill']
            kill['assists'] = participant['assists']
            kill['largestMultiKill'] = participant['largestMultiKill']
            kill['participantId'] = participant['participantId']
            kill['doubleKills'] = participant['doubleKills']
            kill['tripleKills'] = participant['tripleKills']
            kill['quadraKills'] = participant['quadraKills']
            kill['pentaKills'] = participant['pentaKills']
            kill['unrealKills'] = participant['unrealKills']
            kill['kills'] = participant['kills']
            kill['deaths'] = participant['deaths']
            kill['kda'] = challenges['kda']

            kill['dragonKills'] = participant['dragonKills'] # 드래곤에게 죽은 경우
            kill['baronKills'] = participant['baronKills'] # 바론에게 죽은 경우

            data['kill'] = kill
            
            # spell 정보
            spell = {}
            spell['abilityUses'] = challenges['abilityUses']
            spell['spell1Casts'] = participant['spell1Casts']
            spell['spell2Casts'] = participant['spell2Casts']
            spell['spell3Casts'] = participant['spell3Casts']
            spell['spell4Casts'] = participant['spell4Casts']

            data['spell'] = spell

            # damage 정보
            damage = {}
            damage['damagePerMinute'] = challenges['damagePerMinute']
            damage['totalDamageDealt'] = participant['totalDamageDealt']
            damage['totalDamageDealtToChampions'] = participant['totalDamageDealtToChampions']
            damage['totalDamageShieldedOnTeammates'] = participant['totalDamageShieldedOnTeammates']
            damage['totalDamageTaken'] = participant['totalDamageTaken']
            damage['totalHeal'] = participant['totalHeal']
            damage['totalHealsOnTeammates'] = participant['totalHealsOnTeammates']
            damage['totalMinionsKilled'] = participant['totalMinionsKilled']
            damage['totalTimeCCDealt'] = participant['totalTimeCCDealt']
            damage['totalTimeSpentDead'] = participant['totalTimeSpentDead']
            damage['totalUnitsHealed'] = participant['totalUnitsHealed']
            damage['magicDamageDealt'] = participant['magicDamageDealt']
            damage['magicDamageDealtToChampions'] = participant['magicDamageDealtToChampions']
            damage['physicalDamageDealt'] = participant['physicalDamageDealt']
            damage['physicalDamageDealtToChampions'] = participant['physicalDamageDealtToChampions']
            damage['physicalDamageTaken'] = participant['physicalDamageTaken']
            damage['magicDamageTaken'] = participant['magicDamageTaken']

            data['damage'] = damage

            # 터렛 결과
            turret = {}

            turret['firstTowerAssist'] = participant['firstTowerAssist']
            turret['firstTowerKill'] = participant['firstTowerKill']
            turret['turretKills'] = participant['turretKills']
            turret['turretTakedowns'] = participant['turretTakedowns']
            turret['turretsLost'] = participant['turretsLost']

            data['turret'] = turret

            # ward/vision 결과
            ward = {}
            ward['visionClearedPings'] = participant['visionClearedPings']
            ward['visionScore'] = participant['visionScore']
            ward['visionWardsBoughtInGame'] = participant['visionWardsBoughtInGame']
            ward['wardsKilled'] = participant['wardsKilled']
            ward['wardsPlaced'] = participant['wardsPlaced']

            data['ward'] = ward

            # 게임 결과
            data['win'] = participant['win']
            data['gameEndedInEarlySurrender'] = participant['gameEndedInEarlySurrender']
            data['gameEndedInSurrender'] = participant['gameEndedInSurrender']

            reformedParticipants.append(data)

        return Response(result)
    