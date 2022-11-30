
def convertSecondsToTime(duration):
    if duration > 3600:
        hours = duration // 60
        minutes = hours // 60
        seconds = hours % 60
        return f'{hours}시간 {minutes}분 {seconds}초'

    minutes = duration // 60
    seconds = duration % 60

    return f'{minutes}분 {seconds}초'

def convertRawToGamerDictionary(participant):
    
    challenges = participant['challenges']
    data = {}

    # 유저 정보
    info = {}
    info['summonerName'] = participant.get('summonerName', '')
    info['summonerLevel'] = participant.get('summonerLevel', 0)
    info['champLevel'] = participant.get('champLevel', 0)
    info['championId'] = participant.get('championId', 0)
    info['championName'] = participant.get('championName', '')
    info['lane'] = participant.get('lane','')
    
    data['info'] = info

    # jungle 정보
    jungle = {}
    jungle['baronTakedowns'] = challenges.get('baronTakedowns', 0)
    jungle['dragonTakedowns'] = challenges.get('dragonTakedowns', 0)
    jungle['elderDragonMultikills'] = challenges.get('elderDragonMultikills', 0)
    
    data['jungle'] = jungle

    # item/gold 결과
    item = {}
    item['goldEarned'] = participant.get('goldEarned', 0)
    item['goldSpent'] = participant.get('goldSpent', 0)
    item['goldPerMinute'] = challenges.get('goldPerMinute', 0.0)
    item['item0'] = participant.get('item0', 0)
    item['item1'] = participant.get('item1', 0)
    item['item2'] = participant.get('item2', 0)
    item['item3'] = participant.get('item3', 0)
    item['item4'] = participant.get('item4', 0)
    item['item5'] = participant.get('item5', 0)
    item['item6'] = participant.get('item6', 0)
    
    data['item'] = item

    # kill 결과 정보
    kill = {}
    
    kill['firstBloodAssist'] = participant.get('firstBloodAssist', False)
    kill['firstBloodKill'] = participant.get('firstBloodKill', False)
    kill['assists'] = participant.get('assists', 0)
    kill['largestMultiKill'] = participant.get('largestMultiKill', 0)
    kill['participantId'] = participant.get('participantId', 0)
    kill['doubleKills'] = participant.get('doubleKills', 0)
    kill['tripleKills'] = participant.get('tripleKills', 0)
    kill['quadraKills'] = participant.get('quadraKills', 0)
    kill['pentaKills'] = participant.get('pentaKills', 0)
    kill['unrealKills'] = participant.get('unrealKills', 0)
    kill['kills'] = participant.get('kills', 0)
    kill['deaths'] = participant.get('deaths', 0)
    kill['kda'] = challenges.get('kda', 0.0)

    kill['dragonKills'] = participant.get('dragonKills', 0) # 드래곤에게 죽은 경우
    kill['baronKills'] = participant.get('baronKills', 0) # 바론에게 죽은 경우
    
    data['kill'] = kill
    
    # spell 정보
    spell = {}
    spell['abilityUses'] = challenges.get('abilityUses', 0)
    spell['spell1Casts'] = participant.get('spell1Casts', 0)
    spell['spell2Casts'] = participant.get('spell2Casts', 0)
    spell['spell3Casts'] = participant.get('spell3Casts', 0)
    spell['spell4Casts'] = participant.get('spell4Casts', 0)
    
    data['spell'] = spell

    # damage 정보
    damage = {}
    damage['damagePerMinute'] = challenges.get('damagePerMinute', 0.0)
    damage['totalDamageDealt'] = participant.get('totalDamageDealt', 0)
    damage['totalDamageDealtToChampions'] = participant.get('totalDamageDealtToChampions', 0)
    damage['totalDamageShieldedOnTeammates'] = participant.get('totalDamageShieldedOnTeammates', 0)
    damage['totalDamageTaken'] = participant.get('totalDamageTaken', 0)
    damage['totalHeal'] = participant.get('totalHeal', 0)
    damage['totalHealsOnTeammates'] = participant.get('totalHealsOnTeammates', 0)
    damage['totalMinionsKilled'] = participant.get('totalMinionsKilled', 0)
    damage['totalTimeCCDealt'] = participant.get('totalTimeCCDealt', 0)
    damage['totalTimeSpentDead'] = participant.get('totalTimeSpentDead', 0)
    damage['totalUnitsHealed'] = participant.get('totalUnitsHealed', 0)
    damage['magicDamageDealt'] = participant.get('magicDamageDealt', 0)
    damage['magicDamageDealtToChampions'] = participant.get('magicDamageDealtToChampions', 0)
    damage['physicalDamageDealt'] = participant.get('physicalDamageDealt', 0)
    damage['physicalDamageDealtToChampions'] = participant.get('physicalDamageDealtToChampions', 0)
    damage['physicalDamageTaken'] = participant.get('physicalDamageTaken', 0)
    damage['magicDamageTaken'] = participant.get('magicDamageTaken', 0)
    
    data['damage'] = damage

    # 터렛 결과
    turret = {}

    turret['firstTowerAssist'] = participant.get('firstTowerAssist', False)
    turret['firstTowerKill'] = participant.get('firstTowerKill', False)
    turret['turretKills'] = participant.get('turretKills', 0)
    turret['turretTakedowns'] = participant.get('turretTakedowns', 0)
    turret['turretsLost'] = participant.get('turretsLost', 0)
    
    data['turret'] = turret

    # ward/vision 결과
    ward = {}
    ward['visionClearedPings'] = participant.get('visionClearedPings', 0)
    ward['visionScore'] = participant.get('visionScore', 0)
    ward['visionWardsBoughtInGame'] = participant.get('visionWardsBoughtInGame', 0)
    ward['wardsKilled'] = participant.get('wardsKilled', 0)
    ward['wardsPlaced'] = participant.get('wardsPlaced', 0)
    
    data['ward'] = ward

    # 게임 결과
    detail = {}
    detail['win'] = participant.get('win', False)
    detail['gameEndedInEarlySurrender'] = participant.get('gameEndedInEarlySurrender', False)
    detail['gameEndedInSurrender'] = participant.get('gameEndedInSurrender', False)
    
    data['detail'] = detail

    return data