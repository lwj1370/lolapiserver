import os
import pytz

from pytz import timezone
from datetime import datetime
from django.db import DatabaseError, transaction
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from riotwatcher import LolWatcher, ApiError

from .submodels.model_pro_gamer import ProGamer
from .submodels.model_match import GameMatch
from .submodels.model_match_damage import GameDamage
from .submodels.model_match_info import GameInfo
from .submodels.model_match_item import GameItem
from .submodels.model_match_jungle import GameJungle
from .submodels.model_match_kill import GameKill
from .submodels.model_match_spell import GameSpell
from .submodels.model_match_turret import GameTurret
from .submodels.model_match_ward import GameWard
from .submodels.model_match_win_rate import GamerWinRate

from .common.utils import *

class GamerMatchViewSet(APIView):
    def post(self, request, *args, **kwargs):
        print(f'request.GET : {request.GET["nickname"] if "nickname" in request.GET else "Nickname - Not Found"}')
        print(f'request.data : {request.data["nickname"] if "nickname" in request.data else "Nickname - Not Found"}')

        result = {}
        result['match'] = {}
        match = result['match']
        match['matchId'] = 'Not Found'
        match['nickname_validation'] = True

        nickname = request.data["nickname"] if "nickname" in request.data else (request.GET["nickname"] if "nickname" in request.GET else "")

        if(nickname == ""): 
            print('nickname is Empty')
            match['nickname_validation'] = False
            return Response(result)

        pg = ProGamer()

        try:
            pg = ProGamer.objects.get(gamer_nickname=nickname)
            matches = GameMatch.objects.filter(pro_gamer=pg.pk)
            now = datetime.now(timezone('Asia/Seoul'))
            
            lastRequestedTime = matches[len(matches) - 1].requested_time
            
            diff = now - lastRequestedTime
            diffMins = diff.total_seconds() // 60
            
            if diffMins <= 30:
                
                gd = GameDamage.objects.filter(match=matches[0]).values()[0]
                gInfo = GameInfo.objects.filter(match=matches[0]).values()[0]
                gItem = GameItem.objects.filter(match=matches[0]).values()[0]
                gj = GameJungle.objects.filter(match=matches[0]).values()[0]
                gk = GameKill.objects.filter(match=matches[0]).values()[0]
                gs = GameSpell.objects.filter(match=matches[0]).values()[0]
                gt = GameTurret.objects.filter(match=matches[0]).values()[0]
                gw = GameWard.objects.filter(match=matches[0]).values()[0]
                gwr = GamerWinRate.objects.filter(match=matches[0]).values()[0]

                match.update(matches.values()[0])
                match['damage'] = gd
                match['info'] = gInfo
                match['item'] = gItem
                match['jungle'] = gj
                match['kill'] = gk
                match['spell'] = gs
                match['turret'] = gt
                match['ward'] = gw
                match['detail'] = gwr

                return Response(result)

        except ProGamer.DoesNotExist:
            print('프로게이머 정보가 필요합니다.')
        except GameMatch.DoesNotExist:
            print('매치 정보를 찾을 수 없습니다.')
        except ObjectDoesNotExist:
            print('데이터가 비어 있습니다.')
        except Exception as e:
            print(f'Error : {e}')
            return Response(result)
        
        try:
            api_key = os.environ['LOL_API_KEY']

            # riotwatcher 참조
            # https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
            watcher = LolWatcher(api_key)
            region = 'kr'
            
            account = watcher.summoner.by_name(region, nickname)
            matches = watcher.match.matchlist_by_puuid(region, account['puuid'])
            matchInfo = watcher.match.by_id(region, matches[0])['info']
            participants = matchInfo['participants']
            participants = [participant for participant in participants if participant['puuid'] == account['puuid']]
            
            match['matchId'] = matches[0]
            match['startTime'] = datetime.fromtimestamp(matchInfo['gameStartTimestamp'] // 1000, pytz.timezone('Asia/Seoul'))
            match['endTime'] = datetime.fromtimestamp(matchInfo['gameEndTimestamp'] // 1000, pytz.timezone('Asia/Seoul'))
            match['duration'] = convertSecondsToTime(matchInfo['gameDuration'])
            match.update(convertRawToGamerDictionary(participants[0]))

        except ApiError as err:
            print(f'Lol Api Request Failed : {err.response.status_code}')
        except Exception as e:
            print(e)
        except:
            print('Unknown Exception')

        try:
            with transaction.atomic():
                tmpGameMatch = GameMatch()
                tmpGameMatch.pro_gamer = pg
                tmpGameMatch.setJsonData(result['match'])
                GameMatch.save(tmpGameMatch)
                
                tmpGameDamage = GameDamage()
                tmpGameDamage.match = tmpGameMatch
                tmpGameDamage.setJsonData(result['match']['damage'])
                GameDamage.save(tmpGameDamage)

                tmpGameInfo = GameInfo()
                tmpGameInfo.match = tmpGameMatch
                tmpGameInfo.setJsonData(result['match']['info'])
                GameInfo.save(tmpGameInfo)

                tmpGameItem = GameItem()
                tmpGameItem.match = tmpGameMatch
                tmpGameItem.setJsonData(result['match']['item'])
                GameItem.save(tmpGameItem)

                tmpGameJungle = GameJungle()
                tmpGameJungle.match = tmpGameMatch
                tmpGameJungle.setJsonData(result['match']['jungle'])
                GameJungle.save(tmpGameJungle)

                tmpGameKill = GameKill()
                tmpGameKill.match = tmpGameMatch
                tmpGameKill.setJsonData(result['match']['kill'])
                GameKill.save(tmpGameKill)

                tmpGameSpell = GameSpell()
                tmpGameSpell.match = tmpGameMatch
                tmpGameSpell.setJsonData(result['match']['spell'])
                GameSpell.save(tmpGameSpell)

                tmpGameTurret = GameTurret()
                tmpGameTurret.match = tmpGameMatch
                tmpGameTurret.setJsonData(result['match']['turret'])
                GameTurret.save(tmpGameTurret)

                tmpGameWard = GameWard()
                tmpGameWard.match = tmpGameMatch
                tmpGameWard.setJsonData(result['match']['ward'])
                GameWard.save(tmpGameWard)

                tmpGameWinRate = GamerWinRate()
                tmpGameWinRate.match = tmpGameMatch
                tmpGameWinRate.setJsonData(result['match']['detail'])
                GamerWinRate.save(tmpGameWinRate)
            raise DatabaseError('정보 저장에 실패하였습니다.')
        except DatabaseError as e:
            print(e)
        except Exception as e:
            print(e)

        return Response(result)
    